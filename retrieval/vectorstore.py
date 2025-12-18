from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS

class VectorStoreManager:
    def __init__(self):
        self.embeddings = OllamaEmbeddings(model="phi3")
        self.vectorstore = None

    def build(self, documents):
        self.vectorstore = FAISS.from_documents(
            documents,
            self.embeddings
        )

    def similarity_search(self, query, k=3):
        return self.vectorstore.similarity_search(query, k=k)
