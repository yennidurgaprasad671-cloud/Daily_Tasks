"""6. Data Analysis Tool (NumPy + Pandas)
Scenario:
Analyze student marks.
Task:
● Generate marks using NumPy
● Convert into Pandas DataFrame
● Use conditions to filter passing students
● Calculate mean using math/NumPy
● Use loop to print results"""

import numpy as np
import pandas as pd

# Generate 10 random marks between 30 and 100
np.random.seed(42)
marks = np.random.randint(30, 101, size=10)
students = [f"Student_{i+1}" for i in range(len(marks))]

# Convert into Pandas DataFrame
df = pd.DataFrame({"Student": students, "Marks": marks})

# Use condition to filter passing students (pass mark >= 50)
passing_df = df[df["Marks"] >= 50]

# Calculate mean using NumPy
mean_mark = np.mean(df["Marks"])

print(f"Class Mean: {mean_mark:.2f}\n")
print("Passing Students:")

# Use loop to print results
for _, row in passing_df.iterrows():
  print(f"- {row['Student']}: {row['Marks']}")
