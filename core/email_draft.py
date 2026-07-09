import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_email_drafts(situation: str) -> str:
    with open("prompts/email_prompt.txt", "r") as f:
        template = f.read()

    prompt = template.format(situation=situation)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text