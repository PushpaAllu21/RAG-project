
from groq import Groq
import os

from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_answer(query, docs):
    context = "\n\n".join([d.page_content for d in docs])

    prompt = f"""
    You are a biomedical research assistant.

    Use the following research context to answer the question.

    Context:
    {context}

    Question:
    {query}

    Instructions:
    - Give a clear scientific explanation
    - Mention mechanisms if possible
    - Keep it concise
    """

    response = client.chat.completions.create(
        model="llama3-8b-8192",   # fast + free
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content