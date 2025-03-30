# Resume Analyzer (AI-Powered)

Resume Analyzer is a Streamlit web app that uses advanced NLP models and vector embeddings to analyze resumes against job descriptions and offer compatibility scores, matched/unmatched skills, and detailed feedback. Users can also chat with the resume using a conversational AI interface.

## Features

- Upload PDF resumes and input job descriptions
- AI-powered analysis using LLMs via Groq (LLaMA3)
- Generates:
  1. Match percentage
  2. Matched & missing skills
  3. Smart HR insights
- Chat with the resume using semantic search and contextual memory
- Uses vector embeddings (HuggingFace + FAISS)
- Modular structure for easy customization
- Custom dark UI (Streamlit-based)

## Project Structure

├── app.py                  # Entry point

├── frontend/

│   ├── main_app.py         # Resume upload & analysis logic

│   └── chat_interface.py   # Chat-based interaction

├── backend/

│   ├── analysis.py         # Resume analysis logic with Groq

│   ├── pdf_ingestion.py    # PDF reader & text splitter

│   └── vector_store.py     # Embedding + FAISS vector store

├── requirements.txt

└── README.md

## Tech Stack

- Frontend: Streamlit
- Backend: LangChain, Groq LLaMA3
- Embeddings: HuggingFace all-mpnet-base-v2
- Vector Store: FAISS
- PDF Processing: LangChain PyPDFLoader
- How to Run Locally

## Clone the repository

1. Clone the Repository
  - git clone https://github.com/your-username/resume-analyzer.git
  - cd resume-analyzer
2. Set up environment
  - python -m venv venv
  - source venv/bin/activate      # or venv\Scripts\activate (Windows)
  - pip install -r requirements.txt
3. Add your environment variables
  - Create a .env file:
  - GROQ_API_KEY=your_groq_api_key_here
4. Run the app
  - streamlit run app.py

## Future Improvements

- Add support for DOCX format
- Extend compatibility to multiple job roles
- Option to download analysis report as PDF
- Add feedback-based fine-tuning

## Contribution
- PRs are welcome! 
