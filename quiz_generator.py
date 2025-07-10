import google.generativeai as genai
import json
import re

# Replace with your valid Gemini API key
genai.configure(api_key="AIzaSyCyOHpHs2SsRQKAO3PeFg7MAt-2UWfK_ZM")
model = genai.GenerativeModel("models/gemini-1.5-flash")

def generate_mcqs(text):
    prompt = f"""
Act as a quiz generator. Extract as many good multiple-choice questions (MCQs) as possible from the following content.
Each MCQ should have:
- A clear question
- 4 unique options
- 1 correct answer

Return your response in **only** this exact JSON format:
[
  {{
    "question": "What is...",
    "options": ["Option A", "Option B", "Option C", "Option D"],
    "answer": "Option B"
  }},
  ...
]

Here is the content to generate questions from:
{text}
"""

    try:
        response = model.generate_content(prompt)
        output = response.text

        # Extract only the JSON array from response
        match = re.search(r'\[.*\]', output, re.DOTALL)
        if match:
            return json.loads(match.group())
        else:
            print("⚠️ JSON not detected in response.")
    except Exception as e:
        print(f"❌ MCQ generation error: {e}")

    return []

