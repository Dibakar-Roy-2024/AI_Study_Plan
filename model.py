import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
import joblib
#
# # Loading Dataset
df = pd.read_csv('student_study_data.csv')

# # Features and Targets
x = df[["Study Hours Available" , "Past Scores (%)" ,'Exam Date (Days Left)']]
y = df[["Past Scores (%)"]]
#
# # Split data (80% Train, 20% Test)
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2, random_state=42)
#
# # Train Model
model = DecisionTreeRegressor()
model.fit(x_train,y_train)
#
# # Saving the model
joblib.dump(model, "study_plan_model.pkl")
#
print("Model Training Completed And Saved !")

