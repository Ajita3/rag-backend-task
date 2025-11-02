from fastapi import FastAPI
from app.api import ingest, rag  # absolute imports (must match your folder)

app = FastAPI(title="RAG Backend Task")

app.include_router(ingest.router, prefix="/ingest", tags=["ingest"])
app.include_router(rag.router, prefix="/rag", tags=["rag"])

@app.get("/")
async def root():
    return {"status": "ok", "message": "RAG backend running"}
