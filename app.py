import streamlit as st
import tempfile
import os
from langchain_ollama import OllamaLLM
from ingestion.ingest import load_and_split
from retrieval.vectorstore import VectorStoreManager
from explainability.explanation import build_explanation

# LLM Setup
llm = OllamaLLM(
    model="phi3:mini",
    temperature=0.1
)

def generate_answer(query, retrieved_docs):
    """
    Generate an answer using the retrieved documents.

    Args:
        query (str): The user's question.
        retrieved_docs (list): List of retrieved document chunks.

    Returns:
        str: The generated answer.
    """
    if not retrieved_docs:
        return "Answer not found in the provided documents."

    context = "\n\n".join([doc.page_content for doc in retrieved_docs])

    prompt = f"""
You are an academic assistant.
Answer the question using ONLY the context below.
If the context does not contain the information needed to answer the question, say "Answer not found in the provided documents."

Context:
{context}

Question:
{query}

Provide a clear, concise answer.
"""

    response = llm.invoke(prompt)
    return response

# Streamlit UI
st.set_page_config(
    page_title="Explainable RAG Academic Assistant",
    layout="wide",
    page_icon="📘"
)

st.title("📘 Explainable RAG Academic Assistant")

# Sidebar
with st.sidebar:
    st.header("Model Information")
    st.write("**LLM:** Phi-3 Mini via Ollama")
    st.write("**Embeddings:** Phi-3 Mini via Ollama")
    st.write("**Vector Store:** FAISS")

    st.header("PDF Upload")
    uploaded_file = st.file_uploader("Upload a PDF document", type="pdf")

    if uploaded_file is not None:
        if st.button("Ingest Document"):
            with st.spinner("Processing PDF..."):
                # Save uploaded file to temp
                with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
                    tmp_file.write(uploaded_file.getvalue())
                    tmp_path = tmp_file.name

                try:
                    docs = load_and_split(tmp_path)
                    if "vectorstore" not in st.session_state:
                        st.session_state.vectorstore = VectorStoreManager()
                    st.session_state.vectorstore.build(docs)
                    st.success("Document ingested successfully!")
                except Exception as e:
                    st.error(f"Error processing PDF: {str(e)}")
                finally:
                    os.unlink(tmp_path)  # Clean up temp file

# Main area
st.header("Ask a Question")
query = st.text_input("Enter your academic question:")

if query and "vectorstore" in st.session_state:
    with st.spinner("Retrieving and generating answer..."):
        retrieved = st.session_state.vectorstore.similarity_search(query, k=3)
        answer = generate_answer(query, retrieved)
        explanation = build_explanation(retrieved)

    st.subheader("Answer")
    st.write(answer)

    st.subheader("Explainability")
    with st.expander("View Explanation Details"):
        st.write("**Reasoning Summary:**", explanation["reasoning_summary"])
        st.write("**Sources:**")
        for source in explanation["sources"]:
            st.write(f"- {source['pdf_name']} (Page {source['page_number']})")
        st.write(f"**Confidence Score:** {explanation['confidence_score']}")

elif query:
    st.warning("Please upload and ingest a PDF document first.")

st.markdown("---")
st.caption("Built with LangChain, Ollama, and Streamlit for explainable RAG.")
