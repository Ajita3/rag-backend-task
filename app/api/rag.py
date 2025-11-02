from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional, List, Dict
from ..core.embedding_service import embed_text_list
from ..db.vector_db_client import save_to_vector_db  # placeholder
from ..db.metadata_db_client import save_metadata     # optional

router = APIRouter()

# Temporary in-memory chat memory
_conversations: Dict[str, List[Dict]] = {}

class ChatRequest(BaseModel):
    conversation_id: str
    message: str
    top_k: Optional[int] = 5

class ChatResponse(BaseModel):
    reply: str
    sources: List[str] = []

@router.post("/chat", response_model=ChatResponse)
async def chat(req: ChatRequest):
    conv = _conversations.setdefault(req.conversation_id, [])
    
    # Append user message
    conv.append({"role": "user", "content": req.message})
    
    
    chunks = [m["content"] for m in conv[-5:]]  # last 5 messages as demo context
    embeddings = embed_text_list(chunks)
    
   
    reply = f"RAG reply (demo) based on {len(chunks)} recent messages: {req.message}"
    
    conv.append({"role": "assistant", "content": reply})

    sources = [f"doc_{i}" for i in range(len(chunks))]
    
    return ChatResponse(reply=reply, sources=sources)
