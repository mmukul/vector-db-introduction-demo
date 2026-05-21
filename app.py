__import__('pysqlite3')
import sys

# Fix sqlite issue for Chroma
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

import chromadb

# Create persistent Chroma client
client = chromadb.PersistentClient(path="./chroma_db")

# Create or get collection
collection = client.get_or_create_collection(name="demo_collection")

# Add documents
collection.add(
    documents=[
        "DevSecOps improves software security",
        "Chroma is a vector database for AI applications",
        "AI pipelines require security scanning",
        "LangChain helps build LLM applications",
        "Ollama can run LLMs locally"
    ],
    ids=["id1", "id2", "id3", "id4", "id5"]
)

print("Documents added successfully")

# Query documents
results = collection.query(
    query_texts=["What is vector database?"],
    n_results=2
)

print("\nQuery Results:")
print(results)
