import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def summarize_syllabus(syllabus_text: str) -> str:
    with open("prompts/syllabus_prompt.txt", "r") as f:
        template = f.read()

    prompt = template.format(syllabus_text=syllabus_text)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text