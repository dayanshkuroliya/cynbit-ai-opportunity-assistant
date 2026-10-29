from fastapi import APIRouter
from pydantic import BaseModel

from ai.retriever import search_knowledge
from ai.generator import generate_answer

router = APIRouter()


class ChatRequest(BaseModel):
    question: str


@router.post("/chat")
def chat(request: ChatRequest):

    # 1. Search relevant Cynbit information
    results = search_knowledge(
        request.question,
        top_k=3
    )
    if not results:
        return {
            "question": request.question,
            "answer": "I don't have enough information about that.",
            "sources": []
        }

    # 2. Create context from retrieved information
    context = "\n\n".join(
        result["content"]
        for result in results
    )

    # 3. Generate AI answer
    answer = generate_answer(
        request.question,
        context
    )

    # 4. Return clean response
    return {
    "question": request.question,
    "answer": answer,
    "sources": [
        {
            "file": result["filename"],
            "score": round(result["score"], 4)
        }
        for result in results
    ]
}