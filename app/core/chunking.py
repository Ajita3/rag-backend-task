from typing import List, Protocol

class Chunker(Protocol):
    def chunk(self, text: str) -> List[str]:
        ...

class ParagraphChunker:
    def chunk(self, text: str) -> List[str]:
        parts = [p.strip() for p in text.split("\n\n") if p.strip()]
        return parts

class SlidingWindowChunker:
    def __init__(self, words_per_chunk: int = 200, overlap: int = 50):
        self.words_per_chunk = words_per_chunk
        self.overlap = overlap

    def chunk(self, text: str) -> List[str]:
        words = text.split()
        chunks = []
        i = 0
        while i < len(words):
            chunk = words[i:i+self.words_per_chunk]
            chunks.append(" ".join(chunk))
            i += self.words_per_chunk - self.overlap
        return chunks
