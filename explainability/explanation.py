def build_explanation(retrieved_docs):
    """
    Build an explanation for the retrieved documents.

    Args:
        retrieved_docs (list): List of retrieved document chunks.

    Returns:
        dict: Explanation containing reasoning summary, sources, and confidence score.
    """
    if not retrieved_docs:
        return {
            "reasoning_summary": "No relevant context found in the documents.",
            "sources": [],
            "confidence_score": 0.0
        }

    # Extract sources and page numbers
    sources = []
    for doc in retrieved_docs:
        source_info = {
            "pdf_name": doc.metadata.get("source", "Unknown"),
            "page_number": doc.metadata.get("page", "Unknown")
        }
        sources.append(source_info)

    # Simple confidence score based on number of retrieved docs (can be improved)
    confidence_score = min(len(retrieved_docs) / 5.0, 1.0)  # Normalize to 0-1

    # Reasoning summary
    reasoning_summary = f"Retrieved {len(retrieved_docs)} relevant chunks from the uploaded documents to answer the query."

    return {
        "reasoning_summary": reasoning_summary,
        "sources": sources,
        "confidence_score": round(confidence_score, 2)
    }
