import os 
import json 
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(BASE_DIR, "..", "data", "consts", "filter_prompt.txt"), "r") as f:
    SYSTEM_PROMPT = f.read()

def screen_listing(job: dict) -> dict:
    description = "\n".join(f"{k}: {v}" for k, v in job.items())

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=description,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_PROMPT
        )
    )

    try:
        return json.loads(response.text)
    except json.JSONDecodeError: # Gemini sometimes adds unwanted markdown fences
        cleaned = response.text.strip().removeprefix("```json").removesuffix("```")
        return json.loads(cleaned)