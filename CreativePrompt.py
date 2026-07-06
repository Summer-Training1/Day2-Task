from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

response = client.models.generate_content(
    model="gemini-3.1-flash-lite",
    contents="Write a friendly internship request email to an IT department. Start with an exciting opening line about the company's tech work, then ask about internship opportunities",
    config=types.GenerateContentConfig(
        temperature=0.7,
        max_output_tokens=500
    )
)

print(response.text)