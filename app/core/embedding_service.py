
from __future__ import annotations
from typing import List, Iterable
from sentence_transformers import SentenceTransformer
import math


_MODEL_NAME = "all-MiniLM-L6-v2"  
_model: SentenceTransformer | None = None

def _get_model() -> SentenceTransformer:
    global _model
    if _model is None:
        _model = SentenceTransformer(_MODEL_NAME)
    return _model

def embed_text_list(texts: Iterable[str], batch_size: int = 64) -> List[List[float]]:
    
    model = _get_model()
    # sentence-transformers' encode supports batching and returns numpy arrays
    embeddings = model.encode(list(texts), batch_size=batch_size, show_progress_bar=False, convert_to_numpy=True)
    # Convert to plain Python lists for JSON-serializable storage if needed
    return [emb.tolist() for emb in embeddings]
