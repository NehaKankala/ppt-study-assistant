import streamlit as st
from ppt_reader import extract_slide_texts
from explainer import simplify_and_enrich
from quiz_generator import generate_mcq
from pdf_writer import create_study_pdf
import os

st.set_page_config(layout="wide")
st.title("🧠 AI-Powered PPT Explainer and Quiz Generator")

uploaded_ppt = st.file_uploader("📤 Upload your PPT file", type=["pptx"])

if uploaded_ppt:
    with st.spinner("🔍 Extracting and simplifying slides..."):
        slides = extract_slide_texts(uploaded_ppt)
        explanations = [simplify_and_enrich(s) for s in slides if s.strip()]
        st.session_state.explanations = explanations

    st.success("✅ Explanations ready!")

    for i, exp in enumerate(explanations):
        with st.expander(f"Slide {i+1}"):
            st.write(exp)

    if st.button("📄 Generate Study Notes PDF"):
        os.makedirs("static/user_outputs", exist_ok=True)
        pdf_path = "static/user_outputs/study_notes.pdf"
        create_study_pdf(explanations, pdf_path)
        st.success("PDF generated!")
        with open(pdf_path, "rb") as f:
            st.download_button("⬇️ Download Study Notes PDF", f.read(), file_name="study_notes.pdf")

    if st.button("🎮 Generate Quiz from Explanations"):
        with st.spinner("🧠 Generating quiz..."):
            quiz = []
            for e in explanations:
                mcq = generate_mcq(e)
                if mcq and mcq["question"] != "Error generating question" and len(mcq["options"]) == 4:
                    quiz.append(mcq)
        if quiz:
            st.session_state.quiz_data = quiz
            st.session_state.user_answers = [None] * len(quiz)
            st.session_state.quiz_submitted = False
        else:
            st.error("❗ No valid quiz generated")

# --- Display Quiz ---
if "quiz_data" in st.session_state:
    st.header("📝 Take the Quiz")

    for i, mcq in enumerate(st.session_state.quiz_data):
        st.subheader(f"Q{i+1}: {mcq['question']}")
        selected = st.radio(
            f"Select your answer for Q{i+1}",
            mcq['options'],
            key=f"q{i}"
        )
        st.session_state.user_answers[i] = selected

    if st.button("✅ Submit Quiz"):
        st.session_state.quiz_submitted = True

# --- Show Score ---
if st.session_state.get("quiz_submitted", False):
    score = 0
    st.success("🎯 Quiz Results")

    for i, mcq in enumerate(st.session_state.quiz_data):
        user_ans = st.session_state.user_answers[i]
        correct_ans = mcq["answer"]
        st.markdown(f"**Q{i+1}: {mcq['question']}**")
        st.write(f"✅ Correct Answer: `{correct_ans}`")
        st.write(f"🧑 Your Answer: `{user_ans}`")
        st.markdown("---")
        if user_ans == correct_ans:
            score += 1

    st.markdown(f"### 🏆 Your Score: **{score} / {len(st.session_state.quiz_data)}**")

