from ai.retriever import search_knowledge
from ai.generator import generate_answer


question = "What is the weather today?"

results = search_knowledge(
    question,
    top_k=3
)


context = "\n\n".join(
    result["content"]
    for result in results
)


answer = generate_answer(
    question,
    context
)


print("\nUser Question:")
print(question)

print("\nAI Answer:")
print(answer)