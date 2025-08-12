import streamlit as st
import os
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
import google.generativeai as genai

# Load environment variables
load_dotenv()

# --- Configuration ---
FAISS_INDEX_PATH = "faiss_index"
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
API_KEY = os.environ.get("GOOGLE_API_KEY")

# Configure the Google Generative AI client
if not API_KEY:
    st.error("GOOGLE_API_KEY not found in environment variables. Please set it in your .env file.")
    st.stop()
genai.configure(api_key=API_KEY)

# --- Caching Functions ---

# Cache the embedding model
@st.cache_resource
def load_embeddings():
    print("Loading embedding model...")
    embeddings = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL,
        model_kwargs={'device': 'cpu'}
    )
    return embeddings

# Cache the FAISS index
@st.cache_resource
def load_faiss_index(_embeddings):
    print("Loading FAISS index...")
    if not os.path.exists(FAISS_INDEX_PATH):
        st.error(f"Knowledge base ({FAISS_INDEX_PATH}) not found!")
        st.warning("Please run 'python new.py' first to create the vector database.")
        st.stop()
    
    vectordb = FAISS.load_local(
        FAISS_INDEX_PATH, 
        _embeddings, 
        allow_dangerous_deserialization=True
    )
    return vectordb

# --- Core Logic ---

def get_response_from_gemini(question, context):
    """
    Makes a direct API call to the Gemini model with the provided context and question.
    """
    prompt_template = f"""
    Given the following context and a question, generate an answer based on this context only.
    In the answer try to provide as much text as possible from the "context" section without making much changes.
    If the answer is not found in the context, kindly state "I don't know." Don't try to make up an answer.

    CONTEXT:
    {context}

    QUESTION:
    {question}
    """
    
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(prompt_template)
        return response.text
    except Exception as e:
        return f"An error occurred while calling the Gemini API: {e}"

# --- Streamlit App UI ---

st.title("Medical Chatbot 🧑‍⚕️")

# Load resources
embeddings = load_embeddings()
vectordb = load_faiss_index(embeddings)
retriever = vectordb.as_retriever(score_threshold=0.7)

# Get user input
user_question = st.text_input("Ask your medical question:")

if st.button("Get Answer"):
    if user_question:
        with st.spinner("Searching for relevant information..."):
            # 1. Retrieve relevant documents
            relevant_docs = retriever.get_relevant_documents(user_question)
            
            if not relevant_docs:
                st.warning("Could not find relevant information to answer your question.")
            else:
                # 2. Combine the context from all relevant docs
                context = "\n\n".join([doc.page_content for doc in relevant_docs])
                
                with st.spinner("Generating the answer..."):
                    # 3. Get the final answer from Gemini
                    answer = get_response_from_gemini(user_question, context)
                    st.header("Answer")
                    st.write(answer)

                    # Optional: Display source documents
                    with st.expander("Show Sources"):
                        for doc in relevant_docs:
                            st.info(f"Source Question: {doc.metadata['source']}")
    else:
        st.warning("Please enter a question first.")
