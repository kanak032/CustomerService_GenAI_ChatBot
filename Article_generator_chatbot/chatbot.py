import os
import datetime
import subprocess
from dotenv import load_dotenv
import streamlit as st
import google.generativeai as genai
import time
import re

# Loading API Key from .env file
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    st.error("API key not found. Please check your .env file.")
    st.stop()
else:
    genai.configure(api_key=api_key)

model_gemini = genai.GenerativeModel("gemini-2.5-flash")
chat = model_gemini.start_chat(history=[])

# ------------------ Response Functions ------------------

def get_gemini_response(prompt):
    response = chat.send_message(prompt)
    return response

def get_llama3_response(prompt):
    try:
        result = subprocess.run(
            ["ollama", "run", "llama3:8b", prompt],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=180
        )
        return result.stdout.strip() if result.returncode == 0 else f"Error from LLaMA 3: {result.stderr}"
    except Exception as e:
        return f"Exception while calling LLaMA 3: {str(e)}"

def get_mistral_response(prompt):
    try:
        result = subprocess.run(
            ["ollama", "run", "mistral", prompt],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=180
        )
        return result.stdout.strip() if result.returncode == 0 else f"Error from Mistral: {result.stderr}"
    except Exception as e:
        return f"Exception while calling Mistral: {str(e)}"

def save_article(topic, content, model_name):
    os.makedirs("outputs", exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_topic = re.sub(r'\W+', '_', topic.lower())
    filename = f"outputs/{model_name}_{safe_topic}_{timestamp}.txt"
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)

# ------------------ Streamlit UI ------------------

st.set_page_config(page_title="Article Generator Chatbot")
st.title("📝 LLM Article Generator Chatbot")
st.markdown("Generate high-quality articles using Gemini, LLaMA 3, or Mistral.")

model_choice = st.selectbox("Choose LLM Model:", ["Gemini-2.5-Flash", "LLaMA3", "Mistral"])

st.subheader("Select Article Length:")
length = st.selectbox("Choose article length:", ["Short", "Medium", "Long"])
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

topic = st.text_input("Enter an article topic:")
submit = st.button("Generate Article")

# ------------------ Handle Generation ------------------

if submit and topic:
    prompt = f"Write an informative and well-structured article about: {topic}."
    if length == "Short":
        prompt += " Limit the article to around 300 words."
    elif length == "Medium":
        prompt += " Write approximately 500 words."
    else:
        prompt += " Create a detailed long-form article of around 800 words."
    with st.spinner("Generating article..."):
        start_time = time.time()

        if model_choice == "Gemini-2.5-Flash":
            response_chunks = get_gemini_response(prompt)
            full_response = response_chunks.text
            st.write(full_response)
            save_article(topic, full_response, model_name="gemini")

        elif model_choice == "LLaMA3":
            full_response = get_llama3_response(prompt)
            st.write(full_response)
            save_article(topic, full_response, model_name="llama3")

        elif model_choice == "Mistral":
            full_response = get_mistral_response(prompt)
            st.write(full_response)
            save_article(topic, full_response, model_name="mistral")

        elapsed = round(time.time() - start_time, 2)
        st.write(f"🕒 Time taken by {model_choice}: {elapsed} seconds")
        st.session_state.chat_history.append(("YOU", topic))
        st.session_state.chat_history.append((f"BOT ({model_choice})", f"{full_response}\n\n🕒 Time taken: {elapsed} seconds"))

# ------------------ Chat History ------------------

with st.expander("💬 Chat History"):
    for role, text in st.session_state.chat_history:
        st.write(f"**{role}:** {text}")
