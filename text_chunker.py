import re
import os
from typing import List


class TextChunker:
    def __init__(
        self,
        max_words: int = 500,
        overlap_sentences: int = 2
    ):
        self.max_words = max_words
        self.overlap_sentences = overlap_sentences

    def read_txt(self, file_path: str) -> str:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()

    def split_into_sentences(self, text: str) -> List[str]:
        # Split on newlines for transcript format
        sentences = text.strip().split('\n')
        return [s.strip() for s in sentences if s.strip()]

    def chunk_text(self, text: str) -> List[str]:
        sentences = self.split_into_sentences(text)

        chunks = []
        current_chunk = []
        current_word_count = 0

        for i, sentence in enumerate(sentences):
            word_count = len(sentence.split())

            # If adding this sentence exceeds limit → finalize chunk
            if current_word_count + word_count > self.max_words:
                chunks.append(" ".join(current_chunk))

                # Apply overlap (keep last few sentences)
                overlap = current_chunk[-self.overlap_sentences:]
                current_chunk = overlap[:]
                current_word_count = sum(len(s.split()) for s in current_chunk)

            current_chunk.append(sentence)
            current_word_count += word_count

        # Add last chunk
        if current_chunk:
            chunks.append(" ".join(current_chunk))

        return chunks

    def chunk_file(self, file_path: str) -> List[str]:
        text = self.read_txt(file_path)
        return self.chunk_text(text)

    def save_chunks(self, chunks: List[str], output_prefix: str = "chunk"):
        output_dir = "output"
        os.makedirs(output_dir, exist_ok=True)
        for i, chunk in enumerate(chunks, 1):
            file_name = f"{output_prefix}_{i}.txt"
            file_path = os.path.join(output_dir, file_name)
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(chunk)