# Chroma Query Demo

Simple demo project for:
- Chroma Vector Database
- Query Documents
- Semantic Search

## Install

```bash
pip install -r requirements.txt
```

## Run

```bash
python3 app.py
```

## Features

- SQLite fix for Chroma
- Persistent Chroma database
- Add documents
- Semantic query search

## Example Query

```python
results = collection.query(
    query_texts=["What is vector database?"],
    n_results=2
)
```
