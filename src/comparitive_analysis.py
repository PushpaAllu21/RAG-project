from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))



def compare_papers(query, docs):

    context = "\n\n".join([
        f"Title: {d.metadata.get('title')}\n"
        f"PMID: {d.metadata.get('pmid')}\n"
        f"Content: {d.page_content}"
        for d in docs
    ])

    prompt = f"""
    You are a biomedical literature analyst.

    Compare findings across multiple studies.

    Research Question:
    {query}

    Research Context:
    {context}

    Instructions:

    1. Compare study findings
    2. Highlight similarities
    3. Highlight differences
    4. Mention contradictions if present
    5. Mention biological mechanisms
    6. Mention PMIDs for evidence
    7. Keep scientific tone

    Generate structured comparative analysis.
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content
