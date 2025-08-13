# 🤖 CustomerService_GenAI_ChatBot

A modular GenAI-based chatbot designed to handle customer service queries, generate articles using open-source LLMs, answer medical questions using the MedQuAD dataset, and even detect user sentiment for better, emotionally aware responses.

---
#### This repository consists three folder. You can check the README.md for each folder to see the working of each project.

-----

## 📁 Repository Structure

```bash
CustomerService_GenAI_ChatBot/
├── Article_generator_chatbot/       # Task 1: Article generation using open-source LLMs
│   ├── outputs/
|   ├── .env                         # Stores API keys (not uploaded to GitHub)
│   ├── Comparison Study LLMs.pdf    # 📄 Comparison report of 3 open-source LLMs
│   ├── README.md
|   ├── chatbot.py
│   └── requirements.txt 
│
├── Medical Chatbot/                 # Task 2: Medical QnA chatbot using MedQuAD
│   ├── faiss_index/
|   ├── .env                         # Stores API keys (not uploaded to GitHub)
│   ├── README.md
│   ├── app.py
│   ├── medquad_parsed_data.csv
│   ├── parsing.py
│   ├── requirements.txt
│   └── vector_db.ipynb (Colab File to generate Vector Embeddings)
│
├── Sentiment Analysis/             # Task 3: Emotion detection for better chatbot responses
│   ├── faiss_index/
│   ├── .env                        # Stores API keys (not uploaded to GitHub)
|   ├── README.md
|   ├── app.py                        
|   ├── requirements.txt 
└── README.md                       # ← You're here!
