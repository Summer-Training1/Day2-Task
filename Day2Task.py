import sys
sys.stdout.reconfigure(encoding='utf-8')

from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

chat = client.chats.create(
    model="gemini-3.1-flash-lite",
    config=types.GenerateContentConfig(
        temperature=0.7,
        max_output_tokens=500
    )
)

prompts = {
    "Simple Prompt": "Write an email asking for an internship in 120 words",
    "Improved Prompt": "Write a professional email asking for an internship in 120 words",
    "Detailed Prompt": "You are an IT student with Python experience. Write an email to a company's IT department asking about internship openings in 120 words",
    "Creative Prompt": "Write a friendly internship request email to an IT department. Start with an exciting opening line about the company's tech work, then ask about internship opportunities in 120 words",
    "With Constraints Prompt": "You are an IT student. Write a formal email to an IT department requesting an internship. Include your interest in software development, mention basic Python experience, and ask about available positions. Keep it under 120 words and use a polite, professional tone."
}

for label, prompt in prompts.items():
    response = chat.send_message(prompt)
    print(f"\n:{label}")
    print(response.text)