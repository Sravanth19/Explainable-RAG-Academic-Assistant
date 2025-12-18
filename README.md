# 📘 Explainable RAG Academic Assistant

A production-quality, explainable Retrieval-Augmented Generation (RAG) system designed for academic research and question-answering. Built with modern AI tools to provide transparent, source-attributed answers from uploaded PDF documents.

## 🚀 Features

- **PDF Upload & Processing**: Seamlessly upload and process academic PDFs
- **Intelligent Retrieval**: Uses FAISS vector store with Phi-3 Mini embeddings for accurate document retrieval
- **Explainable Answers**: Provides reasoning summaries, source citations, and confidence scores
- **Hallucination Prevention**: Answers strictly based on retrieved context
- **Modern UI**: Clean, professional Streamlit interface with sidebar and expandable explanations
- **Modular Architecture**: Well-structured code suitable for interviews and portfolio showcase

## 🏗️ Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   PDF Upload    │───▶│   Ingestion     │───▶│   Vector Store   │
│   (Streamlit)   │    │   (LangChain)   │    │   (FAISS)        │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Query Input   │───▶│   Retrieval     │───▶│   Generation    │
│   (Streamlit)   │    │   (Similarity)  │    │ (Phi-3 Mini LLM) │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Answer        │    │   Explanation   │    │   Sources       │
│   Display       │    │   Summary       │    │   & Confidence  │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **LLM**: Phi-3 Mini via Ollama (lightweight, efficient)
- **Embeddings**: Phi-3 Mini via Ollama (consistent, RAM-efficient)
- **Vector Store**: FAISS
- **Document Processing**: LangChain (PyPDFLoader, RecursiveCharacterTextSplitter)
- **Programming Language**: Python 3.8+

## 📋 Prerequisites

1. **Ollama Installation**: Download and install Ollama from [ollama.ai](https://ollama.ai)
2. **Required Models**: Pull the Phi-3 Mini model in Ollama:
   ```bash
   ollama pull phi3:mini    # For both LLM and embeddings (lightweight)
   ```
3. **Python Environment**: Python 3.8 or higher

## 🏃‍♂️ How to Run

1. **Clone the Repository**:
   ```bash
   git clone <your-repo-url>
   cd explainable-rag-academic-assistant
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Start Ollama Server** (in a separate terminal):
   ```bash
   ollama serve
   ```

4. **Run the Application**:
   ```bash
   streamlit run app.py
   ```

5. **Access the App**: Open your browser to `http://localhost:8501`

## 💡 How It Works

1. **Document Ingestion**:
   - Upload a PDF document via the sidebar
   - The system chunks the document into manageable pieces (500 chars with 100 overlap)
   - Generates embeddings using Phi-3 Mini and stores them in FAISS vector store

2. **Question Answering**:
   - User inputs an academic question
   - System retrieves top-3 most relevant document chunks
   - Phi-3 Mini LLM generates an answer strictly from the retrieved context
   - If no relevant context is found, responds with "Answer not found"

3. **Explainability**:
   - **Reasoning Summary**: Explains how many chunks were retrieved
   - **Sources**: Lists PDF name and page numbers for each retrieved chunk
   - **Confidence Score**: Calculated based on number of retrieved documents (0-1 scale)

## 📝 Sample Questions

Try asking questions like:
- "What are the main findings of this research?"
- "Explain the methodology used in the study."
- "What are the limitations mentioned in the paper?"
- "Summarize the conclusion of this academic work."

## 🔮 Future Improvements

- **Multi-Document Support**: Allow ingestion of multiple PDFs simultaneously
- **Advanced Chunking**: Implement semantic chunking for better retrieval
- **Citation Integration**: Add direct PDF page links and highlights
- **Conversation History**: Maintain context across multiple questions
- **Model Fine-tuning**: Fine-tune Mistral on academic domain data
- **Evaluation Metrics**: Implement ROUGE/BLEU scores for answer quality
- **Cloud Deployment**: Containerize and deploy on cloud platforms

## 📊 Validation Checklist

- [x] App runs without ModuleNotFoundError
- [x] Mistral responds correctly via Ollama
- [x] PDF ingestion works seamlessly
- [x] Explainability output displays properly
- [x] UI is clean and professional
- [x] No hallucinations - answers based only on context
- [x] Modular, readable, interview-ready code

## 🤝 Contributing

This project is designed to showcase AI/ML engineering skills. Feel free to fork, modify, and use it in your portfolio or job applications.

## 📄 License

MIT License - feel free to use this project for educational and professional purposes.

---

**Built by [Your Name]** - AI/ML Engineer Portfolio Project
