import os
import numpy as np

from ai.embeddings import create_embedding


KNOWLEDGE_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
    "knowledge"
)


def load_documents():
    documents = []

    for filename in os.listdir(KNOWLEDGE_DIR):

        if filename.endswith(".md"):

            path = os.path.join(
                KNOWLEDGE_DIR,
                filename
            )

            with open(path, "r", encoding="utf-8") as file:
                content = file.read()

            documents.append({
                "filename": filename,
                "content": content
            })

    return documents


def split_text(text, chunk_size=150, overlap=30):

    words = text.split()
    chunks = []

    start = 0

    while start < len(words):

        end = start + chunk_size

        chunk = " ".join(
            words[start:end]
        )

        chunks.append(chunk)

        start += chunk_size - overlap

    return chunks


def cosine_similarity(vector_a, vector_b):

    a = np.array(vector_a)
    b = np.array(vector_b)

    denominator = (
        np.linalg.norm(a) *
        np.linalg.norm(b)
    )

    if denominator == 0:
        return 0.0

    return np.dot(a, b) / denominator


def keyword_score(query, text):

    query_words = set(
        query.lower().split()
    )

    text_words = set(
        text.lower().split()
    )

    if not query_words:
        return 0.0

    matches = query_words.intersection(
        text_words
    )

    return len(matches) / len(query_words)


# -------------------------------------------------
# LOAD AND EMBED KNOWLEDGE ONCE
# -------------------------------------------------

print("Loading Cynbit knowledge...")

documents = load_documents()

knowledge_chunks = []

for document in documents:

    chunks = split_text(
        document["content"]
    )

    for chunk in chunks:

        embedding = create_embedding(
            chunk
        )

        knowledge_chunks.append({
            "filename": document["filename"],
            "content": chunk,
            "embedding": embedding
        })


print(
    f"Loaded {len(knowledge_chunks)} knowledge chunks."
)


# -------------------------------------------------
# SEARCH
# -------------------------------------------------

def search_knowledge(
    query,
    top_k=3,
    min_score=0.65
):

    # Only the user's query is embedded now.
    query_embedding = create_embedding(
        query
    )

    file_results = {}

    for chunk in knowledge_chunks:

        semantic_score = cosine_similarity(
            query_embedding,
            chunk["embedding"]
        )

        keyword_boost = keyword_score(
            query,
            chunk["content"]
        )

        final_score = (
            semantic_score +
            (0.2 * keyword_boost)
        )

        result = {
            "filename": chunk["filename"],
            "content": chunk["content"],
            "score": float(final_score)
        }

        filename = chunk["filename"]

        # Keep only the best chunk
        # from each file.
        if (
            filename not in file_results
            or final_score >
            file_results[filename]["score"]
        ):
            file_results[filename] = result

    results = list(
        file_results.values()
    )

    results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    results = [
        result
        for result in results
        if result["score"] >= min_score
    ]

    return results[:top_k]