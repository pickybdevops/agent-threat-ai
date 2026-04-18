from __future__ import annotations

from typing import Any, Dict

try:
    import chromadb
    from sentence_transformers import SentenceTransformer
except Exception:  # pragma: no cover
    chromadb = None
    SentenceTransformer = None

_model = None
_collection = None
_mem_store: Dict[str, str] = {}


def _get_collection():
    global _model, _collection
    if chromadb is None or SentenceTransformer is None:
        return None, None
    if _model is None:
        _model = SentenceTransformer("all-MiniLM-L6-v2")
    if _collection is None:
        client = chromadb.Client()
        _collection = client.get_or_create_collection("threats")
    return _model, _collection


def store(description: str, cve_id: str) -> None:
    model, collection = _get_collection()
    if model is None or collection is None:
        _mem_store[cve_id] = description
        print(f"[Memory] Stored fallback record for {cve_id}")
        return

    embedding = model.encode(description).tolist()
    try:
        collection.upsert(documents=[description], embeddings=[embedding], ids=[cve_id])
    except AttributeError:
        # Some versions may not expose upsert; emulate with delete/add.
        try:
            collection.delete(ids=[cve_id])
        except Exception:
            pass
        collection.add(documents=[description], embeddings=[embedding], ids=[cve_id])


def search(query: str, top_k: int = 2) -> Any:
    model, collection = _get_collection()
    if model is None or collection is None:
        matches = [v for _, v in list(_mem_store.items())[:top_k]]
        return {"documents": [matches], "ids": [list(_mem_store.keys())[:top_k]]}

    embedding = model.encode(query).tolist()
    return collection.query(query_embeddings=[embedding], n_results=top_k)
