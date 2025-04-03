import pandas as pd

# Loading Dataset
df = pd.read_csv('student_study_data.csv')

# Check first 5 rows
print(df.head())

# Check for missing values
print(df.isnull().sum())

# Fill missing values if any
df.fillna(method='ffill', inplace=True)

print("Data has been Loaded and Cleaned Successfully !")


