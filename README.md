# Chroma Query Demo

Simple demo project for:
- Chroma Vector Database
- Query Documents
- Semantic Search

# Installation Steps

## Step 1 — Clone Repository

```bash
git clone https://github.com/mmukul/vector-db-introduction-demo.git
```

## Step 2 — Move into Project Directory

```bash
cd vector-db-introduction-demo
```

## Step 3 — Create Virtual Environment (Recommended)

### Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

## Step 4 — Install Dependencies

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install chromadb sentence-transformers
```

## Step 5 — Run the Demo

```bash
python app.py
```

## Expected Output

The system performs semantic similarity search and returns the most relevant documents.

Example:

```text
Pizza is an Italian food
Pasta is made using sauce
```
