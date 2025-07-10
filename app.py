import streamlit as st
from ppt_reader import extract_slide_texts,extract_pdf_texts
from explainer import simplify_and_enrich
from quiz_generator import generate_mcqs
from pdf_writer import create_study_pdf
import os

st.set_page_config(layout="wide")
st.title("🧠 AI-Powered PPT Explainer, Quiz & Avatar Guide")

if uploaded_file:
    with st.spinner("🔍 Extracting and simplifying content..."):
        file_type = uploaded_file.name.split('.')[-1].lower()

        if file_type == 'pptx':
            slides = extract_slide_texts(uploaded_file)
        elif file_type == 'pdf':
            slides = extract_pdf_texts(uploaded_file)
        else:
            st.error("❌ Unsupported file type")
            st.stop()

        combined_text = "\n".join(slides)
        explanation = simplify_and_enrich(combined_text)
        st.session_state.explanation = explanation

    st.success("✅ Explanation complete!")

    # --- Explanation Display ---
    with st.expander("🧾 Complete Explanation"):
        st.write(st.session_state.explanation)

    # --- Study Notes PDF ---
    if st.button("📄 Generate Study Notes PDF"):
        os.makedirs("static/user_outputs", exist_ok=True)
        pdf_path = "static/user_outputs/study_notes.pdf"
        create_study_pdf([st.session_state.explanation], pdf_path)
        st.success("📘 PDF generated!")
        with open(pdf_path, "rb") as f:
            st.download_button("⬇️ Download Study Notes PDF", f.read(), file_name="study_notes.pdf")

    # --- Quiz Generator ---
    if st.button("🎮 Generate Quiz from Explanation"):
        with st.spinner("Generating quiz..."):
            quiz = generate_mcqs(st.session_state.explanation)
        if quiz:
            st.session_state.quiz_data = quiz
            st.session_state.user_answers = [None] * len(quiz)
            st.session_state.quiz_submitted = False
        else:
            st.warning("❗ No valid quiz generated.")

# --- Quiz Section ---
if "quiz_data" in st.session_state:
    st.header("📝 Take the Quiz")

    for i, mcq in enumerate(st.session_state.quiz_data):
        st.subheader(f"Q{i+1}: {mcq['question']}")
        selected = st.radio(
            f"Select your answer for Q{i+1}",
            mcq['options'],
            key=f"q{i}",
            index=None
        )
        st.session_state.user_answers[i] = selected

    if st.button("✅ Submit Quiz"):
        st.session_state.quiz_submitted = True

# --- Score Display ---
if st.session_state.get("quiz_submitted", False):
    score = 0
    st.success("🎯 Quiz Results")

    for i, mcq in enumerate(st.session_state.quiz_data):
        user_ans = st.session_state.user_answers[i]
        correct_ans = mcq["answer"]
        st.markdown(f"**Q{i+1}: {mcq['question']}**")
        st.write(f"✅ Correct Answer: `{correct_ans}`")
        st.write(f"🧑 Your Answer: `{user_ans or 'Not answered'}`")
        st.markdown("---")
        if user_ans == correct_ans:
            score += 1

    st.markdown(f"### 🏆 Your Score: **{score} / {len(st.session_state.quiz_data)}**")

