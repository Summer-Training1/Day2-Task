from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

response = client.models.generate_content(
    model="gemini-3.1-flash-lite",
    contents="You are a IT student with Python experience. Write an email to a company's IT department asking about internship openings ",
    config=types.GenerateContentConfig(
        temperature=0.7,
        max_output_tokens=500
    )
)

print(response.text)