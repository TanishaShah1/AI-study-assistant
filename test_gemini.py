import os
from dotenv import load_dotenv
from google import genai

load_dotenv() #this opens .env in the current folder and loads GEMINI_API_KEY into the environment.

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Say hello and confirm you're working, in one sentence."
)

print(response.text)