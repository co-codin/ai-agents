import openai, json
import os
from dotenv import load_dotenv

load_dotenv()

client = openai.OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)
messages = []

def call_ai():
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
    )
    message = response.choices[0].message.content
    messages.append({
        "role": "assistant",
        'content': message,
    })
    print(f"AI: {message}")


while True:
    message = input("Send a message to LLM")
    if message == "q":
        break
    else:
        messages.append({
            "role": "user",
            'content': message,
        })
        print(f"User: {message}")
        call_ai()