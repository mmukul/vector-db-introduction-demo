# ChromaDB Vector Database Demo

Simple Vector Database demo using ChromaDB and Python.

This project demonstrates:

- Vector Databases
- Semantic Search
- Similarity Search
- Embeddings
- ChromaDB Basics

---

# What is a Vector Database?

Traditional databases search based on exact keywords.

Vector Databases search based on meaning and similarity.

Example:

Query:
Looking for nearby pizza shop

Stored Document:
Pizza available nearby

Even though the words are different, Vector Databases understand the semantic meaning.

---

# Install Dependencies

Install ChromaDB:

```bash
pip install chromadb
```

If you face SQLite compatibility issues on Linux:

```bash
pip install pysqlite3-binary
```

---

# Project Structure

```bash
demo-app.py
README.md
```

---

# Run the Demo

```bash
python demo-app.py
```

---

# Expected Output

ChromaDB returns the most relevant matching documents based on semantic similarity.

Example:

```bash
Pizza available nearby
```

---

# Persistent Storage Example

To save vectors permanently:

```python
import chromadb

client = chromadb.PersistentClient(path="./my_vectordb")
```

This stores the vector database locally on disk.

---

# Real World Use Cases

- AI Chatbots
- RAG Applications
- AI Search Engines
- Recommendation Systems
- AI Assistants
- LLM Applications

---

# Technologies Used

- Python
- ChromaDB
- Vector Embeddings
- Semantic Search

---
