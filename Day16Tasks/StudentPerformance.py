"""1. Student Performance Dashboard
Scenario:
A school records marks of students in one subject:
marks = np.array([45, 67, 89, 56, 72, 91, 38])
students = ["A", "B", "C", "D", "E", "F", "G"]
Task:
● Convert to Pandas DataFrame
● Plot:
○ Line graph → trend of marks
○ Bar chart → student vs marks
○ Pie chart → Pass (>50) vs Fail
○ Histogram → distribution of marks
○ Scatter plot → index vs marks
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Data
marks = np.array([45, 67, 89, 56, 72, 91, 38])
students = ["A", "B", "C", "D", "E", "F", "G"]

# 1. Convert to Pandas DataFrame
df1 = pd.DataFrame({"Student": students, "Marks": marks})
df1["Status"] = np.where(df1["Marks"] > 50, "Pass", "Fail")

# Plotting
fig, axes = plt.subplots(2, 3, figsize=(15, 8))
fig.suptitle("1. Student Performance Dashboard", fontsize=16, fontweight="bold")

# Line graph -> trend of marks
axes[0, 0].plot(df1["Student"], df1["Marks"], marker="o", color="blue")
axes[0, 0].set_title("Trend of Marks")
axes[0, 0].set_ylabel("Marks")

# Bar chart -> student vs marks
axes[0, 1].bar(df1["Student"], df1["Marks"], color="skyblue")
axes[0, 1].set_title("Student vs Marks")
axes[0, 1].set_ylabel("Marks")

# Pie chart -> Pass (>50) vs Fail
status_counts = df1["Status"].value_counts()
axes[0, 2].pie(
    status_counts,
    labels=status_counts.index,
    autopct="%1.1f%%",
    colors=["lightgreen", "salmon"],
)
axes[0, 2].set_title("Pass (>50) vs Fail")

# Histogram -> distribution of marks
axes[1, 0].hist(df1["Marks"], bins=5, color="purple", edgecolor="black")
axes[1, 0].set_title("Distribution of Marks")
axes[1, 0].set_xlabel("Marks")
axes[1, 0].set_ylabel("Frequency")

# Scatter plot -> index vs marks
axes[1, 1].scatter(df1.index, df1["Marks"], color="red")
axes[1, 1].set_title("Index vs Marks")
axes[1, 1].set_xlabel("Index")
axes[1, 1].set_ylabel("Marks")

axes[1, 2].axis("off")  # Hide empty subplot
plt.tight_layout()
plt.show()
