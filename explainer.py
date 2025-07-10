import os
import google.generativeai as genai

# Set your Gemini API key
GOOGLE_API_KEY = "AIzaSyCyOHpHs2SsRQKAO3PeFg7MAt-2UWfK_ZM"
genai.configure(api_key=GOOGLE_API_KEY)

# ✅ Use the correct model ID from Google Gemini API
model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")  # Fast & free

def simplify_and_enrich(all_slides_text):
    prompt = f"""
You are an expert educator. Read the following collection of PowerPoint slide contents and generate a single, continuous explanation in a simple, easy-to-understand way.

- Do not break the explanation by slide number.
- Combine and logically organize the concepts as if you're explaining to a beginner.
- Add real-life examples, analogies, and simple comparisons where necessary.
- Avoid technical jargon unless needed, and explain it if used.
- Make the tone friendly and informative.

Here is the slide content:
\"\"\"
{all_slides_text}
\"\"\"

Now give the full explanation:
"""
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"❌ Error generating explanation: {e}"


