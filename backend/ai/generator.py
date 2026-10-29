from transformers import pipeline


MODEL_NAME = "HuggingFaceTB/SmolLM2-360M-Instruct"


generator = pipeline(
    "text-generation",
    model=MODEL_NAME,
    device=-1
)


def generate_answer(question, context):

    prompt = f"""<|im_start|>system
You are Cynbit AI Assistant.

Answer the user's question using ONLY the information provided.

Rules:
- Answer directly.
- Keep the answer short.
- Do not repeat the same item.
- If you list items, mention each item only once.
- Do not ask another question.
- Do not invent information.
<|im_end|>

<|im_start|>user
CYNBIT INFORMATION:

{context}

QUESTION:
{question}
<|im_end|>

<|im_start|>assistant
"""

    result = generator(
        prompt,
        max_new_tokens=35,
        do_sample=False,
        return_full_text=False
    )

    answer = result[0]["generated_text"].strip()

    return answer