def update_embedding(cve_id, new_desc):
    from memory.vector_store import store
    store(new_desc, cve_id)
    print(f"[Feedback] Updated context for {cve_id}")
