from ai.embeddings import create_embedding
from ai.retriever import load_documents

documents = load_documents()

print("Documents found:", len(documents))

text = documents[0]["content"]

embedding = create_embedding(text)

print("Embedding size:", len(embedding))
print("First 5 values:", embedding[:5])