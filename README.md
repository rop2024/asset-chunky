# Asset Chunky

A small Python utility that splits large text files into smaller overlapping chunks.

## What it does

1. Reads `.txt` files from the `input/` folder
2. Splits text into sentences (one per line)
3. Groups sentences into chunks capped at a configurable word count
4. Optionally overlaps chunks by carrying forward the last N sentences
5. Writes each chunk to `output/chunk_N.txt`

This is useful for breaking long documents (transcripts, notes, articles) into manageable pieces for processing, embedding, or analysis.

## Files

- `text_chunker.py` — `TextChunker` class with chunking logic
- `base.py` — entry point; processes the first `.txt` file in `input/`
- `input/` — drop your `.txt` source files here
- `output/` — generated `chunk_N.txt` files go here

## Usage

```bash
# Place a text file in input/
# Run
python base.py
```

Output: `N chunks created` plus `chunk_1.txt`, `chunk_2.txt`, ... in `output/`.

## Configuration

Edit `base.py`:

```python
chunker = TextChunker(
    max_words=2000,        # max words per chunk
    overlap_sentences=3    # sentences carried over between chunks
)
```

Defaults: `max_words=500`, `overlap_sentences=2`.

## Requirements

Python 3.x only — no external dependencies.