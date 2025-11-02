from typing import ByteString
from pypdf import PdfReader
import io

def extract_text_from_pdf(pdf_bytes: ByteString) -> str:
    reader = PdfReader(io.BytesIO(pdf_bytes))
    texts = []
    for page in reader.pages:
        try:
            texts.append(page.extract_text() or "")
        except Exception:
            texts.append("")
    return "\n\n".join(texts)
