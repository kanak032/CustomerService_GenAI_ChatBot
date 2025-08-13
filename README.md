# 🤖 CustomerService_GenAI_ChatBot

A modular GenAI-based chatbot designed to handle customer service queries, generate articles using open-source LLMs, answer medical questions using the MedQuAD dataset, and even detect user sentiment for better, emotionally aware responses.

---
#### This repository consists three folder. You can check the README.md for each folder to see the working of each project.

-----

## 📁 Repository Structure

```bash
CustomerService_GenAI_ChatBot/
├── article_generator_chatbot/       # Task 1: Article generation using open-source LLMs
│   ├── mistral_generator.py
│   ├── llama_generator.py
│   ├── README.md
│   └── LLM_Comparison_Document.pdf  # 📄 Comparison report of 3 open-source LLMs
│
├── medical_chatbot/                 # Task 2: Medical QnA chatbot using MedQuAD
│   ├── streamlit_app.py
│   ├── medquad_model.pkl
│   └── utils/
│
├── sentiment_analysis/             # Task 3: Emotion detection for better chatbot responses
│   ├── sentiment_analysis.py
│
├── .env                            # Stores API keys (not uploaded to GitHub)
├── requirements.txt
└── README.md                       # ← You're here!
