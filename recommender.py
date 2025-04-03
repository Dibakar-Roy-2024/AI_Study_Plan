import pandas as pd
import joblib

# ✅ Load the trained model
model = joblib.load("study_plan_model.pkl")

# 📌 Get user input
study_hours = float(input("📚 Enter available study hours per day: "))
past_scores = float(input("📊 Enter your past percentage scores: "))
exam_days_left = int(input("📅 Enter number of days left for the exam: "))

# ✅ Convert input into DataFrame (for valid feature names)
new_student_data = pd.DataFrame([{
    "Study Hours Available": study_hours,
    "Past Scores (%)": past_scores,
    "Exam Date (Days Left)": exam_days_left
}])

# 🔍 Predict estimated score
predicted_score = model.predict(new_student_data)[0]

# 📝 Generate Study Plan
if predicted_score >= 90:
    study_plan = "🚀 Excellent! Keep revising key concepts and solve past papers."
elif predicted_score >= 75:
    study_plan = "📖 Focus on weak topics and practice more numerical problems."
elif predicted_score >= 50:
    study_plan = "📌 Increase study hours and make summary notes for revision."
else:
    study_plan = "⚠️ You need to study hard! Follow a strict schedule and seek help if needed."

# 🎯 Display Recommendation
print("\n🎯 **Your AI-Generated Study Plan:**")
print("📊 Estimated Score:", round(predicted_score, 2), "%")
print("📌 Recommended Study Plan:", study_plan)
