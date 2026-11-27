"""8. Complex DataFrame Transformation
A DataFrame:
df = pd.DataFrame({
"Name": ["A", "B", "C", "D"],
"Marks": [50, 80, 30, 90]
})
Scenario:
● Students scoring below 50 failed
Task:
1. Create a column Status ("Pass"/"Fail")
2. Filter only passed students
3. Calculate average marks of passed students"""
import numpy as np
import pandas as pd

# 1. Create the DataFrame
df = pd.DataFrame({"Name": ["A", "B", "C", "D"], "Marks": [50, 80, 30, 90]})

# Task 1: Create the 'Status' column ('Pass' if Marks >= 50, else 'Fail')
df["Status"] = np.where(df["Marks"] >= 50, "Pass", "Fail")
print("Updated DataFrame:")
print(df)

# Task 2: Filter only passed students
passed_students = df[df["Status"] == "Pass"]
print("\nPassed Students:")
print(passed_students)

# Task 3: Calculate average marks of passed students
average_marks = passed_students["Marks"].mean()
print(f"\nAverage Marks of Passed Students: {average_marks:.2f}")
