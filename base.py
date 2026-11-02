from text_chunker import TextChunker
import os

chunker = TextChunker(
    max_words=2000,
    overlap_sentences=3
)

input_dir = "input"
files = os.listdir(input_dir)
txt_files = [f for f in files if f.endswith('.txt')]
txt_files.sort()
if txt_files:
    input_file = os.path.join(input_dir, txt_files[0])
    chunks = chunker.chunk_file(input_file)
else:
    print("No .txt files found in input folder")
    chunks = []

if chunks:
    print(f"{len(chunks)} chunks created")

    # Optional: save to files
    chunker.save_chunks(chunks, output_prefix="chunk")