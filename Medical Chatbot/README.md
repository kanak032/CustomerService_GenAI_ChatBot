# 🩺 Medical Q\&A Chatbot

## 📖 Overview

This project is a **smart medical chatbot** designed to provide reliable health-related answers using the **MedQuAD dataset**. It combines **intelligent retrieval** and **natural language generation** to give accurate and readable responses. The chatbot features a simple, user-friendly interface built using **Streamlit**.

---

## ✨ Features

* ✅ **Accurate Medical Answers**
  Provides detailed responses grounded in trusted medical data from the MedQuAD dataset.

* ⚡ **Intelligent Retrieval System**
  Utilizes a **FAISS** vector database to quickly fetch the most relevant medical passages.

* 🤖 **Natural Language Generation**
  Leverages **Google’s Gemini** model to generate clean, human-like responses from retrieved text.

* 🖥️ **Streamlit Web Interface**
  Clean and intuitive UI for seamless interaction, suitable for both technical and non-technical users.

* 🔍 **Source Verification**
  Displays the source documents used to generate each answer, ensuring transparency and traceability.

---

## 🛠️ Setup and Installation

Follow the steps below to set up the project on your local system.

### 1. 📋 Prerequisites

* Python `3.10`(To avoid dependencied conflict)
* A Google API Key for Gemini (if you want to use your own)

---

### 2. 📥 Clone the Repository

```bash
git clone https://github.com/kanak032/CustomerService_GenAI_ChatBot.git
cd CustomerService_GenAI_ChatBot
cd Medical Chatbot
```

---

### 3. 🧪 Set Up the Environment

It's strongly recommended to use a virtual environment:

```bash
# Create a virtual environment
python -m venv venv

# Activate it
# On Windows:
.\venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

---

### 4. 📦 Install Dependencies

Install required Python libraries:

```bash
pip install -r requirements.txt
```

---

### 5. 🔐 Set Up Your API Key(If you have your own API)

If you’re using **Google’s Gemini model**, create a `.env` file in the root folder:

```bash
GOOGLE_API_KEY="your_secret_api_key_goes_here"
```



---

### ▶️ Run the App

Start the Streamlit app using:

```bash
streamlit run app.py
```

---

## 📚 Dataset

* The chatbot is powered by the **[MedQuAD dataset](https://github.com/abachaa/MedQuAD )**, which includes curated medical Q\&A content from trusted sources.

---

## 📌 License

This project is for educational and research purposes. Please refer to the respective licenses of Gemini, FAISS, and MedQuAD if deploying for commercial use.

---

