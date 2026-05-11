import os 
import json 
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(BASE_DIR, "..", "data", "consts", "filter_prompt.txt"), "r") as f:
    SYSTEM_PROMPT = f.read()

def screen_listing(job: dict) -> dict:
    description = "\n".join(f"{k}: {v}" for k, v in job.items())

    response = model.generate_content(f"{SYSTEM_PROMPT}\n\nDescription:\n{description}")

    try:
        return json.loads(response.text)
    except json.JSONDecodeError: # Gemini sometimes adds unwanted markdown fences
        cleaned = response.text.strip().removeprefix("```json").removesuffix("```")
        return json.loads(cleaned)