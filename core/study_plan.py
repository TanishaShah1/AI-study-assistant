import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_study_plan(notes: str) -> str:
    with open("prompts/study_plan_prompt.txt", "r") as f:
        template = f.read()

    prompt = template.format(notes=notes)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text