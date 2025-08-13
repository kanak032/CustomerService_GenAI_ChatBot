import streamlit as st
import os
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
import google.generativeai as genai
from transformers import pipeline
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# --- Load Environment Variables ---
load_dotenv()

# --- Configuration ---
FAISS_INDEX_PATH = "faiss_index"  #faiss_index folder path goes here. Make sure path is correct !!!!!!!!!
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
API_KEY = os.environ.get("GOOGLE_API_KEY")

# --- Initial Setup and Checks ---
# Configure the Google Generative AI client
if not API_KEY:
    st.error("GOOGLE_API_KEY not found in environment variables. Please create a .env file with your key.")
    st.stop()
genai.configure(api_key=API_KEY)

# --- Caching Functions (to load models only once) ---

@st.cache_resource
def load_vader():
    print("Loading VADER sentiment lexicon...")
    try:
        nltk.data.find('sentiment/vader_lexicon.zip')
    except LookupError:
        nltk.download('vader_lexicon')
    return SentimentIntensityAnalyzer()

@st.cache_resource
def load_bert_sentiment_model():
    print("Loading BERT sentiment analysis model...")
    return pipeline("sentiment-analysis", model="distilbert/distilbert-base-uncased-finetuned-sst-2-english")

@st.cache_resource
def load_embeddings():
    print("Loading embedding model...")
    return HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL, model_kwargs={'device': 'cpu'})

@st.cache_resource
def load_faiss_index(_embeddings):
    print("Loading FAISS index...")
    if not os.path.exists(FAISS_INDEX_PATH):
        st.error(f"Knowledge base ({FAISS_INDEX_PATH}) not found in this folder!")
        st.warning("Please copy the 'faiss_index' folder from your original project into this one.")
        st.stop()
    return FAISS.load_local(FAISS_INDEX_PATH, _embeddings, allow_dangerous_deserialization=True)

# --- Core Logic Functions ---

def analyze_sentiment_vader(text, sia):
    score = sia.polarity_scores(text)
    if score['compound'] >= 0.05: return "positive"
    elif score['compound'] <= -0.05: return "negative"
    else: return "neutral"

def analyze_sentiment_bert(text, model):
    result = model(text)[0]
    if result['label'] == 'POSITIVE': return "positive"
    elif result['label'] == 'NEGATIVE': return "negative"
    else: return "neutral"

def get_response_from_gemini(question, context):
    prompt_template = f"""
    Given the following context and a question, generate an answer based on this context only.
    If the answer is not found, state "I don't know."

    CONTEXT: {context}
    QUESTION: {question}
    """
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(prompt_template)
        return response.text
    except Exception as e:
        return f"An error occurred while calling the Gemini API: {e}"

# --- Streamlit App UI ---
st.title("Medical Chatbot with Sentiment Analysis 🧑‍⚕️")

st.sidebar.title("Options")
sentiment_model_choice = st.sidebar.selectbox(
    "Choose Sentiment Analysis Model",
    ("BERT (Accurate)", "VADER (Fast)")
)

# Load resources
embeddings = load_embeddings()
vectordb = load_faiss_index(embeddings)
retriever = vectordb.as_retriever(score_threshold=0.7)

if sentiment_model_choice == "BERT (Accurate)":
    sentiment_analyzer = load_bert_sentiment_model()
else:
    sentiment_analyzer = load_vader()

user_question = st.text_input("Ask your medical question:")

if st.button("Get Answer"):
    if user_question:
        with st.spinner("Analyzing sentiment..."):
            if sentiment_model_choice == "BERT (Accurate)":
                sentiment = analyze_sentiment_bert(user_question, sentiment_analyzer)
            else:
                sentiment = analyze_sentiment_vader(user_question, sentiment_analyzer)
        
        if sentiment == 'negative':
            st.info("I understand this may be a difficult or worrying topic. Let's find some information to help.")
        elif sentiment == 'positive':
            st.info("It's great that you're feeling positive! Let's get you the information you're looking for.")

        with st.spinner("Searching for relevant information..."):
            relevant_docs = retriever.get_relevant_documents(user_question)
            
            if not relevant_docs:
                st.warning("Could not find relevant information to answer your question.")
            else:
                context = "\n\n".join([doc.page_content for doc in relevant_docs])
                with st.spinner("Generating the answer..."):
                    answer = get_response_from_gemini(user_question, context)
                    st.header("Answer")
                    st.write(answer)
                    with st.expander("Show Sources"):
                        for doc in relevant_docs:
                            st.info(f"Source Question: {doc.metadata['source']}")
    else:
        st.warning("Please enter a question first.")

