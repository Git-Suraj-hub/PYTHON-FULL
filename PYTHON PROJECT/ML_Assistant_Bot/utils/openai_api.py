import openai
import os
openai.api_key = os.getenv("OPEN_API_KEY")

def ask_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
    )
    return response['choices'][0]['message']['content']
