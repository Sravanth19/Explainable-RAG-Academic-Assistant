# 🎓 Explainable RAG Academic Assistant

An intelligent research companion that allows users to upload academic PDFs and receive answers with a built-in explainability layer, using **Phi-3 Mini** and **RAG (Retrieval-Augmented Generation)**.

---

## 🖼️ Project Execution & Output Screenshots

The following screenshots demonstrate the **end-to-end execution flow** of the assistant running locally on **Streamlit (localhost)**, from PDF ingestion to explainable answer generation.

### 1️⃣ Application Interface & PDF Upload (Localhost)
![Application Interface](PASTE_IMAGE_PERMALINK_HERE)

**Description:** This screenshot shows the initial Streamlit user interface. It includes model information (LLM, Embeddings, Vector Store) and the PDF upload section. The system is ready to ingest academic documents.

### 2️⃣ Successful PDF Ingestion & System Readiness
![PDF Ingestion Completed](PASTE_IMAGE_PERMALINK_HERE)

**Description:** Demonstrates successful PDF ingestion. The document is loaded, chunked, converted into embeddings using Phi-3 Mini, and stored in the FAISS vector database.

### 3️⃣ Explainable RAG Question Answering Output
![Explainable RAG Output](PASTE_IMAGE_PERMALINK_HERE)

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
