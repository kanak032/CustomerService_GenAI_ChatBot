# 🧑‍⚕️ Medical Q&A Chatbot with Sentiment Analysis

This project is an advanced, empathetic question-answering chatbot designed to provide **medical information** while being sensitive to the **user's emotional state**. It leverages the **MedQuAD dataset** as its knowledge base and integrates **sentiment analysis** to tailor responses. The application is built using a clean and intuitive web interface in **Streamlit**.

---

## ✨ Features

- **Accurate Medical Answers:**  
  Provides detailed responses based on the content of the MedQuAD dataset.

- **Empathetic Responses:**  
  Detects the user's emotional tone (positive, negative, or neutral) and offers appropriate, reassuring messages before answering.

- **Dual Sentiment Models:**  
  Choose between two sentiment analysis options via sidebar:
  - **BERT (Accurate):** Deep-learning based model for precise sentiment detection.
  - **VADER (Fast):** Lexicon-based model for lightweight and quick analysis.

- **Intelligent Retrieval:**  
  Uses a **FAISS** vector database to find the most relevant medical context for a question.

- **Natural Language Generation:**  
  Uses **Google's Gemini** model to generate clear, human-readable answers.

- **Simple Web Interface:**  
  Built using **Streamlit**, ensuring a smooth and user-friendly experience.

- **Source Verification:**  
  Displays original source documents from which the answers are generated.

---

## 🚀 Setup and Installation

Follow the steps below to get the chatbot running on your local machine.

### 1. Prerequisites

- Python 3.10(Must use to avoid dependencies conflicts)
- A Google API Key for the Gemini model(If you have your own)

---

### 2. 📥 Clone the Repository

```bash
git clone https://github.com/kanak032/CustomerService_GenAI_ChatBot.git
cd CustomerService_GenAI_ChatBot
cd Sentiment Analysis
```


### 3. Set Up the Environment

Using a virtual environment is highly recommended:

```bash

# Create virtual environment
python -m venv venv
```
#### Activate environment
```bash
# On Windows:
.\venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### 4. Install Dependencies
Install all required packages:
```bash
pip install -r requirements.txt
### 5. Set Up Your API Key(If you are using your own)
Create a .env file in the project root and add your Gemini API key:

GOOGLE_API_KEY="your_secret_api_key_goes_here"

### ▶️ Usage Instructions
Run the chatbot using Streamlit:

```bash
streamlit run app.py
```
This will open the chatbot in your browser. You can ask medical questions and switch between sentiment models using the sidebar.
### Questions to try:
**Negative Sentiment (Should show an understanding message)**

1. "I'm so scared about these chest pains, what could be wrong?"

2. "I'm really worried, I've been losing weight for no reason."

3. "My child has a high fever and I'm panicking, what should I do?"

4. "This constant joint pain is making my life miserable."

**Positive Sentiment (Should show an encouraging message)**

1. "I'm feeling great and want to learn about vitamins to stay healthy!"

2. "My check-up went well! Can you tell me more about maintaining a healthy heart?"

3. "I'm excited to start a new fitness plan, what are some good exercises for beginners?"

**Neutral Sentiment (Should show NO extra message)**

1. "What is the definition of a parasite?"

2. "How is blood pressure measured?"

3. "List the types of headaches."

### 🛠 Technologies Used
Category	    ->Tools/Technologies
Backend       ->	Python
Web Framework ->	Streamlit
LLM	          ->Google Gemini (gemini-1.5-flash)
Vector Store  ->	FAISS
Embeddings	   ->sentence-transformers/all-MiniLM-L6-v2
Sentiment Models->	- BERT: distilbert-base-uncased-finetuned-sst-2-english
                   - VADER (NLTK)
Core Libraries   ->	LangChain, Pandas, Transformers, NLTK

### 📌 Note
Gemini API is required for generating answers. Ensure the key is valid and usage limits are not exceeded.
Ensure that the directory contain faiss_index folder

📄 License
This project is for educational and research purposes only. Always consult a licensed medical professional for actual health concerns.









