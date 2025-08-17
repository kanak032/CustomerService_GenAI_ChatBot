# 🧠 Generative AI Article Comparison using Open-Source LLMs

---

## 📌 Project Overview

We evaluate and compare the article generation capabilities of the following open-source LLMs:

- **LLaMA 3**
- **Mistral**
- **Gemini**

Each model was prompted with the same topic(Generative AI). The generated articles were stored in the outputs folder

---

## 🧠 Technologies & Libraries

- Python 3.10 (⚠️ *Required for dependency compatibility*)
- [Streamlit](https://streamlit.io/) 
- [Transformers](https://huggingface.co/transformers/)
- [Google Generative AI](https://ai.google.dev/)

---

## 📁 Project Structure
📦Article_generator_chatbot/
┣ 📄 outputs/
┃ ┣ gemini_generative_ai_20250811_231548.txt
┃ ┣ llama3_generative_ai_20250811_231702.txt
┃ ┗ mistral_generative_ai_20250811_231817.txt
┣ 📄chatbot.py
┣ 📄 requirements.txt
┗ 📄 README.md


---

## ⚙️ Setup Instructions

> **Python Version Required:** `Python 3.10`

### 1. 📥 Clone the Repository

```bash
git clone https://github.com/kanak032/CustomerService_GenAI_ChatBot.git
cd Article_generator_chatbot
```
### 2.Create a Virtual Environment (Optional but Recommended)
```bash
python3.10 -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate     # For Windows
```
### 3.Install Dependencies
```bash
pip install -r requirements.txt
```
###  Ollama Setup (For LLaMA3 and Mistral support)
##### 1. Download and install Ollama:
   https://ollama.com/download
##### 2. Ensure Ollama is Running
After installation:
Make sure the Ollama is running in the background.
Verify by running the following command in your terminal or command prompt:
```bash
ollama --version
```
##### 3. Pull Required Models
This project uses the following large language models:
->llama3:8b
->mistral
Pull them using the commands below:
```bash
ollama pull llama3:8b
ollama pull mistral
```
##### 4.Verify Installation (Optional)
To test if the models are working:
```bash
ollama run llama3:8b
```
or
```bash
ollama run mistral
```
ℹ️ Note: The models are stored locally after pulling and do not require internet once downloaded.
### ▶️ How to Run:
Run the following command on your terminal:
```bash
streamlit run chatbot.py
``` 
### 📊 Output
All generated articles are stored under the outputs/ directory

## 📌 Notes

- **Mistral** and **LLaMA 3** models were run locally using Ollama
- **Gemini** was accessed via the Google Generative AI SDK using an API key and requires internet connectivity.
- All models were given the **same prompt** for consistency in article generation.
- The outputs were saved in `.txt` files and later compared for coherence, relevance, and structure.


