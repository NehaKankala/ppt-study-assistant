# 🧠 AI-Powered PPT Study Assistant

This is a Streamlit-based web application that helps users understand PowerPoint presentations more effectively. It uses generative AI to extract text from `.pptx` files, simplify content, generate study notes, and create quizzes.

---

## 🚀 Features

- 📂 Upload any `.pptx` file
- 🔍 Extract and simplify slide text using Gemini AI
- 📄 Generate a downloadable study notes PDF
- 🎮 Generate interactive MCQ quizzes from slides
- 📝 Take the quiz, get instant feedback, and view your score

---

## 🛠️ Tech Stack

- `Python`
- `Streamlit` for frontend UI
- `Gemini API (Google Generative AI)`
- `python-pptx` for reading PPT files
- `FPDF` for PDF generation

---

## 🧪 How to Run

1. Clone the repository:

```bash
git clone https://github.com/NehaKankala/ppt-study-assistant.git
cd ppt-study-assistant

2. Create a virtual environment and activate:

python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

3.Install dependencies:

pip install -r requirements.txt

4.Set up your environment variable for Gemini API:

export GOOGLE_API_KEY="your-gemini-api-key"

5.Run the app:

streamlit run app.py
