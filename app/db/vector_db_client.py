

def save_to_vector_db(texts, embeddings):
    
    print("Saving to vector DB...")
    for i, (text, emb) in enumerate(zip(texts, embeddings)):
        print(f"Chunk {i}: '{text[:50]}...' with embedding length {len(emb)}")
    return True
