"""
MindPrint - Vector Store & Embeddings
"""

class VectorStore:
    def __init__(self):
        self.store_name = "MindPrint Vector DB"
        self.documents = []
    
    def add_document(self, text: str, metadata: dict = None):
        """Add document to vector store"""
        doc = {
            "id": len(self.documents) + 1,
            "content": text,
            "metadata": metadata or {},
            "mindprint_tag": f"MP-DOC-{len(self.documents) + 1}"
        }
        self.documents.append(doc)
        return doc["mindprint_tag"]
    
    def search(self, query: str, top_k: int = 3):
        """Simple keyword search (replace with embeddings later)"""
        results = []
        for doc in self.documents:
            if any(word.lower() in doc["content"].lower() for word in query.split()):
                results.append(doc)
        return results[:top_k]
    
    def get_stats(self):
        return {
            "total_docs": len(self.documents),
            "store": self.store_name
        }

# Example
if __name__ == "__main__":
    vs = VectorStore()
    vs.add_document("Human code has unique patterns and creativity")
    print(vs.get_stats())
