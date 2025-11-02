from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from typing import Optional
from app.schemas.ingest_schemas import IngestResponse
from app.core.text_extractor import extract_text_from_pdf
from app.core.chunking import ParagraphChunker, SlidingWindowChunker
from app.core.embedding_service import embed_text_list
from app.db.vector_db_client import save_to_vector_db
from app.db.metadata_db_client import save_metadata

router = APIRouter()

@router.post("/upload", response_model=IngestResponse)
async def upload_document(
    file: UploadFile = File(...),
    chunk_strategy: Optional[str] = Form("paragraph")
):
    filename = file.filename.lower()
    if not (filename.endswith(".pdf") or filename.endswith(".txt")):
        raise HTTPException(status_code=400, detail="Only .pdf and .txt allowed")

    content = await file.read()
    text = ""
    if filename.endswith(".txt"):
        try:
            text = content.decode("utf-8")
        except UnicodeDecodeError:
            text = content.decode("latin-1")
    else:
        text = extract_text_from_pdf(content)

    # Select chunker
    if chunk_strategy == "paragraph":
        chunker = ParagraphChunker()
    elif chunk_strategy == "sliding":
        chunker = SlidingWindowChunker()
    else:
        raise HTTPException(status_code=400, detail="Invalid chunk_strategy")

    chunks = chunker.chunk(text)

    return IngestResponse(document_id="doc_dummy_1", chunks=len(chunks), message="Uploaded with chunking")
