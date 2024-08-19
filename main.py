import os
import openai
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


openai.api_key = os.environ.get('OPENAI_API_KEY')


completion = openai.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "user",
            "content": "How do I output all files in a directory using Python?",
        },
    ],
)
print(completion.choices[0].message.content)