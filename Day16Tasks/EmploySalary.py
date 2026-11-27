"""3. Employee Salary Insights
Scenario:
salaries = np.array([25000, 30000, 28000, 40000, 50000, 35000])
departments = ["HR", "IT", "HR", "IT", "Sales", "Sales"]
Task:
● Convert into DataFrame
● Plot:
○ Line graph → salary trend
○ Bar chart → department-wise salary comparison
○ Pie chart → department distribution
○ Histogram → salary distribution
○ Scatter plot → index vs salary """

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Data
salaries = np.array([25000, 30000, 28000, 40000, 50000, 35000])
departments = ["HR", "IT", "HR", "IT", "Sales", "Sales"]

# 1. Convert into DataFrame
df3 = pd.DataFrame({"Department": departments, "Salary": salaries})

# Plotting
fig, axes = plt.subplots(2, 3, figsize=(15, 8))
fig.suptitle("3. Employee Salary Insights", fontsize=16, fontweight="bold")

# Line graph -> salary trend
axes[0, 0].plot(df3.index, df3["Salary"], marker="o", color="navy")
axes[0, 0].set_title("Salary Trend")
axes[0, 0].set_xlabel("Employee Index")
axes[0, 0].set_ylabel("Salary")

# Bar chart -> department-wise salary comparison (Average Salary)
dept_avg_salary = df3.groupby("Department")["Salary"].mean()
axes[0, 1].bar(
    dept_avg_salary.index,
    dept_avg_salary.values,
    color=["coral", "lightblue", "lightgreen"],
)
axes[0, 1].set_title("Department-wise Avg Salary")
axes[0, 1].set_ylabel("Average Salary")

# Pie chart -> department distribution
dept_counts = df3["Department"].value_counts()
axes[0, 2].pie(dept_counts, labels=dept_counts.index, autopct="%1.1f%%")
axes[0, 2].set_title("Department Distribution")

# Histogram -> salary distribution
axes[1, 0].hist(df3["Salary"], bins=4, color="slateblue", edgecolor="black")
axes[1, 0].set_title("Salary Distribution")
axes[1, 0].set_xlabel("Salary")
axes[1, 0].set_ylabel("Frequency")

# Scatter plot -> index vs salary
axes[1, 1].scatter(df3.index, df3["Salary"], color="crimson")
axes[1, 1].set_title("Index vs Salary")
axes[1, 1].set_xlabel("Index")
axes[1, 1].set_ylabel("Salary")

axes[1, 2].axis("off")
plt.tight_layout()
plt.show()
