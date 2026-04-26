import os
from groq import Groq

client = Groq(
    api_key=os.getenv("GROQ_API_KEY"))

def summarize_news(text):

    prompt = f"""
    You are a news intelligence agent.
    
    From the following multi-source news headlines (BBC, Reuters, CNN),
    identify the 5 most important global stories and summarize them clearly.
    
    Headlines:
    {text}
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
    )

    return response.choices[0].message.content