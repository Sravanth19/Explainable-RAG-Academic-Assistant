# 🎓 Explainable RAG Academic Assistant

An intelligent research companion that allows users to upload academic PDFs and receive answers with a built-in explainability layer, using **Phi-3 Mini** and **RAG (Retrieval-Augmented Generation)**.

---

## 🖼️ Project Execution & Output Screenshots

The following screenshots demonstrate the **end-to-end execution flow** of the assistant running locally on **Streamlit (localhost)**, from PDF ingestion to explainable answer generation.

### 1️⃣ Application Interface & PDF Upload (Localhost)
![Application Interface](https://github.com/Sravanth19/Explainable-RAG-Academic-Assistant/blob/d922aef9aeb0b8a7647b563eb3de92d567c87fa7/pic.png)

**Description:** This screenshot shows the initial Streamlit user interface. It includes model information (LLM, Embeddings, Vector Store) and the PDF upload section. The system is ready to ingest academic documents.

### 2️⃣ Successful PDF Ingestion & System Readiness
![PDF Ingestion Completed](https://github.com/Sravanth19/Explainable-RAG-Academic-Assistant/blob/3315a8f70579b77a3d4e07a66978cf1621e6d017/pic1.png)

**Description:** Demonstrates successful PDF ingestion. The document is loaded, chunked, converted into embeddings using Phi-3 Mini, and stored in the FAISS vector database.

### 3️⃣ Explainable RAG Question Answering Output
![Explainable RAG Output](https://github.com/Sravanth19/Explainable-RAG-Academic-Assistant/blob/18b6bc85f3b1d86b4d6e3eedba3f48809a60bfbb/pic2.png)

**Description:** Shows the core functionality: the user asks a question, relevant chunks are retrieved, and an answer is generated strictly from the context. The explainability layer displays source references and a confidence score.

---

## 📐 System Architecture Workflow

The diagram below illustrates the data flow and component interaction within the assistant.

```text
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   PDF Upload    │───▶│   Ingestion     │───▶│   Vector Store  │
│   (Streamlit)   │    │   (LangChain)   │    │   (FAISS)       │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                      │                      │
         ▼                      ▼                      ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Query Input   │───▶│   Retrieval     │───▶│   Generation    │
│   (Streamlit)   │    │   (Similarity)  │    │ (Phi-3 Mini LLM)│
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                      │                      │
         ▼                      ▼                      ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Answer        │    │   Explanation   │    │   Sources       │
│   Display       │    │   Summary       │    │   & Confidence  │
└─────────────────┘    └─────────────────┘    └─────────────────┘

```

## 🛠️ Tech Stack

- **Frontend:** Streamlit  
- **LLM:** Phi-3 Mini via Ollama (lightweight, efficient)  
- **Embeddings:** Phi-3 Mini via Ollama (consistent, RAM-efficient)  
- **Vector Store:** FAISS  
- **Document Processing:** LangChain (PyPDFLoader, RecursiveCharacterTextSplitter)  
- **Programming Language:** Python 3.8+

---

## 📋 Prerequisites

1. **Ollama Installation**  
   Download and install Ollama from:  
   👉 https://ollama.ai

2. **Required Model**  
   Pull the Phi-3 Mini model:
   ```bash
   ollama pull phi3
   ```
## 🐍 Python Environment

- **Python Version:** 3.8 or higher

---

## 🏃‍♂️ How to Run

### 1️⃣ Clone the Repository
```bash
git clone <your-repo-url>
cd Explainable-RAG-Academic-Assistant

```


### 3️⃣ Start Ollama Server

```bash
ollama serve
```
### 4️⃣ Run the Application
```bash
streamlit run app.py

```
### 5️⃣ Access the App

-Open your browser at:
```bash

👉 http://localhost:8501
```


## 💡 How It Works

### 📄 Document Ingestion
- Upload a PDF document via the sidebar
- The system chunks the document into smaller sections
- Embeddings are generated using **Phi-3 Mini**
- All embeddings are stored in a **FAISS vector database**

### ❓ Question Answering
- Retrieves top-k relevant document chunks
- Generates answers **strictly from retrieved context**
- Prevents hallucinations by refusing unsupported answers

### 🔍 Explainability
- Provides a reasoning summary
- Displays source citations with page numbers
- Includes a confidence score for transparency

---

## 📝 Sample Questions

- *"What are the main findings of this research?"*  
- *"Explain the methodology used in the study."*  
- *"What are the limitations mentioned in the paper?"*  
- *"Summarize the conclusion of this academic work."*

---

## 🔮 Future Improvements

- Multi-PDF ingestion and comparison  
- Semantic chunking for better contextual understanding  
- Direct citation highlighting inside PDFs  
- Conversation memory (chat history support)

---

## 📊 Validation Checklist

- [x] App runs without `ModuleNotFoundError`  
- [x] PDF ingestion and chunking works correctly  
- [x] Explainability output (Sources & Confidence) is visible  
- [x] Lightweight model optimized for low-RAM systems  
- [x] Clean, modular, interview-ready code  

---
**Built by [Gutipalli sravanth]** 
