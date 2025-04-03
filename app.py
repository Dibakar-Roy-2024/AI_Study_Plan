import streamlit as st
import pandas as pd
import joblib
import time
from streamlit_extras.let_it_rain import rain

# 🎨 Page Configuration
st.set_page_config(page_title="AI Study Plan", page_icon="📚", layout="wide")

# 🌟 CSS Styling
st.markdown("""
    <style>
    body {background-color: #f5f7fa; font-family: 'Arial', sans-serif;}
    .title {text-align: center; font-size: 36px; font-weight: bold; color: #2c3e50;}
    .subtitle {text-align: center; font-size: 22px; color: #7f8c8d;}
    .box {border-radius: 10px; padding: 20px; background: #ecf0f1; box-shadow: 3px 3px 10px rgba(0,0,0,0.2);}
    .number {font-size: 20px; font-weight: bold; color: #3498db;}
    .footer {text-align: center; font-size: 16px; margin-top: 30px; color: #7f8c8d;}
    </style>
""", unsafe_allow_html=True)

# 🏫 Title with Animation
st.markdown('<h1 class="title">📚 AI-Generated Personalized Study Plan</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Your Smart Study Guide for Exam Success 🚀</p>', unsafe_allow_html=True)

# 🎊 Rain Effect (Just for Fun!)
rain(emoji="📖", font_size=20, falling_speed=5, animation_length="infinite")

# ✅ Load Model
model = joblib.load("study_plan_model.pkl")

# 📝 User Inputs
st.markdown('<div class="box">', unsafe_allow_html=True)

st.markdown('<p class="number">1️⃣ Study Hours Per Day:</p>', unsafe_allow_html=True)
study_hours = st.slider(" ", 1, 12, 5)

st.markdown('<p class="number">2️⃣ Past Percentage Scores:</p>', unsafe_allow_html=True)
past_scores = st.slider(" ", 0, 100, 75)

st.markdown('<p class="number">3️⃣ Days Left for Exam:</p>', unsafe_allow_html=True)
exam_days_left = st.slider(" ", 1, 90, 15)

st.markdown('</div>', unsafe_allow_html=True)

# 🎯 Predict Button
if st.button("🚀 Generate My Study Plan"):
    with st.spinner("⏳ Analyzing Your Study Strategy..."):
        time.sleep(2)  # Animation delay

        # ✅ Prepare Input Data
        new_student_data = pd.DataFrame([{
            "Study Hours Available": study_hours,
            "Past Scores (%)": past_scores,
            "Exam Date (Days Left)": exam_days_left
        }])

        # 🔍 Predict Score
        predicted_score = model.predict(new_student_data)[0]

        # 📌 Generate Study Plan
        if predicted_score >= 90:
            study_plan = "🔥 Excellent! Keep revising key concepts and solve past papers."
            color = "green"
        elif predicted_score >= 75:
            study_plan = "📖 Focus on weak topics and practice more numerical problems."
            color = "blue"
        elif predicted_score >= 50:
            study_plan = "📌 Increase study hours and make summary notes for revision."
            color = "orange"
        else:
            study_plan = "⚠️ You need to study hard! Follow a strict schedule and seek help if needed."
            color = "red"

        # 📊 Show Results with Progress Bar
        st.markdown(f'<h2 style="color:{color};">📊 Estimated Score: {round(predicted_score, 2)}%</h2>',
                    unsafe_allow_html=True)
        st.progress(min(int(predicted_score), 100))

        # 📌 Show Study Plan
        st.info(f"📌 **Recommended Study Plan:** {study_plan}")

# 🎉 Footer
st.markdown('<p class="footer">🚀 Powered by AI | Made with ❤️ for Students</p>', unsafe_allow_html=True)
