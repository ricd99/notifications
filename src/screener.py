"""
Module containing function that filters listings with an LLM based on SYSTEM PROMPT
"""
import os 
import json 
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(BASE_DIR, "..", "data", "consts", "filter_prompt.txt"), "r") as f:
    SYSTEM_PROMPT = f.read()

def screen_listing(job: dict) -> dict:
    description = "\n".join(f"{k}: {v}" for k, v in job.items())

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": description},
        ]
    )

    text = response.choices[0].message.content

    try:
        return json.loads(text) 
    except json.JSONDecodeError: # Gemini sometimes adds unwanted markdown fences
        cleaned = text.strip().removeprefix("```json").removesuffix("```")
        return json.loads(cleaned)