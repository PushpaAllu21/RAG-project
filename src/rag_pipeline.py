
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def generate_answer(query, docs):

    context = "\n\n".join([
        f"PMID: {d.metadata.get('pmid')}\n"
        f"Title: {d.metadata.get('title')}\n"
        f"Content: {d.page_content}"
        for d in docs
    ])

    prompt = f"""
    You are a biomedical research assistant.

    Use ONLY the provided research context.

    Context:
    {context}

    Question:
    {query}

    Instructions:
    - Give evidence-based answers
    - Mention biological mechanisms
    - Cite PMIDs in the answer
    - Do not hallucinate
    - Keep response concise
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content
