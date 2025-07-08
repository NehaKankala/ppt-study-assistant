import google.generativeai as genai
import json
import re

genai.configure(api_key="AIzaSyCpN_U0zXU80WFrs0s9qWVfxxA1GvvuHDQ")
model = genai.GenerativeModel("gemini-1.5-flash")

def generate_mcq(text):
    prompt = f"""
Generate one multiple choice question from this text with 4 options and the correct answer in JSON format:
{text}
Respond exactly in this format:
{{
  "question": "...",
  "options": ["...", "...", "...", "..."],
  "answer": "..."
}}
"""
    try:
        response = model.generate_content(prompt)
        output = response.text
        match = re.search(r'\{.*\}', output, re.DOTALL)
        if match:
            return json.loads(match.group())
    except Exception as e:
        print(f"MCQ generation error: {e}")
    return {"question": "Error generating question", "options": [], "answer": ""}

