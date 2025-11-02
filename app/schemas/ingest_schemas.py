from pydantic import BaseModel

class IngestResponse(BaseModel):
    document_id: str
    chunks: int
    message: str
