import os
import google.generativeai as genai

# Set your Gemini API key
GOOGLE_API_KEY = "AIzaSyCpN_U0zXU80WFrs0s9qWVfxxA1GvvuHDQ"
genai.configure(api_key=GOOGLE_API_KEY)

# ✅ Use the correct model ID from Google Gemini API
model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")  # Fast & free

def simplify_and_enrich(text):
    prompt = f"""
You are an educational assistant. Given a technical topic, respond with:

1. 📘 Definition  
2. 🧠 Simple explanation  
3. 💡 Real-life example or analogy  

Topic: {text}
"""
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error generating explanation: {str(e)}"

