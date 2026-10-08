import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

while True:
    query = input("Ask: ")
    if query == "q":
        break

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {"role": "system", "content": "Give direct, concise answers in 1-2 sentences without intro, lists, or tables."},
            {"role": "user", "content": query}
        ]
    )

    print("Ai Response: ", response.choices[0].message.content)