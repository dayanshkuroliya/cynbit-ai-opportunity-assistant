from ai.retriever import search_knowledge


query = "What is the weather today?"

results = search_knowledge(query)


print("\nUser Question:")
print(query)

print("\nRelevant Knowledge:\n")

for result in results:
    print("File:", result["filename"])
    print("Score:", round(result["score"], 4))
    print()