import os
from huggingface_hub import InferenceClient

# Create Hugging Face inference client
client = InferenceClient(
    model="meta-llama/Meta-Llama-3-8B-Instruct",
    token=os.getenv("HUGGINGFACE_API_KEY")
)

def ask_llm(prompt):
    try:
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are a professional coding assistant. Always return complete, executable code."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            max_tokens=600,       # increased to reduce cut-off
            temperature=0.2
        )

        output = response.choices[0].message.content

        # Simple check for incomplete code (missing braces)
        if output.count("{") != output.count("}"):
            output += "\n\n⚠️ WARNING: The code may be incomplete. Please regenerate."

        return output

    except Exception as e:
        return f"Error from Hugging Face: {e}"