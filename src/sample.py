from typing import Final
import os
from dotenv import load_dotenv
from openai import OpenAI
# THIS IS A TEST FILE
load_dotenv()
OPENAI_API_KEY: Final[str] = os.getenv('OPENAI_API_KEY')

open_ai_client = OpenAI()

chat_log = []
chat_log.append({
    "role": "user", 
        "content": "say this is a test"
})
output = open_ai_client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{
        "role": "user", 
        "content": "say this is a test"
    }]
    )
completion = output.choices[0].message.content
print(completion)