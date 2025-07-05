import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")
chroma_client = chromadb.Client()
collection = chroma_client.get_or_create_collection("threats")

def store(description, cve_id):
    embedding = model.encode(description).tolist()
    collection.add(documents=[description], embeddings=[embedding], ids=[cve_id])

def search(query, top_k=2):
    embedding = model.encode(query).tolist()
    return collection.query(query_embeddings=[embedding], n_results=top_k)
