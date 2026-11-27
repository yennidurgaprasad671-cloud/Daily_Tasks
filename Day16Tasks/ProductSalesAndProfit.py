"""5. Product Sales & Profit Analysis
Scenario:
sales = np.array([200, 300, 250, 400, 350])
profit = np.array([50, 70, 60, 90, 80])
products = ["A", "B", "C", "D", "E"]
Task:
● Create DataFrame
● Plot:
○ Line graph → sales trend
○ Bar chart → product vs sales
○ Pie chart → sales contribution
○ Histogram → profit distribution
○ Scatter plot → sales vs profit """

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Data
sales = np.array([200, 300, 250, 400, 350])
profit = np.array([50, 70, 60, 90, 80])
products = ["A", "B", "C", "D", "E"]

# 1. Create DataFrame
df5 = pd.DataFrame({"Product": products, "Sales": sales, "Profit": profit})

# Plotting
fig, axes = plt.subplots(2, 3, figsize=(15, 8))
fig.suptitle("5. Product Sales & Profit Analysis", fontsize=16, fontweight="bold")

# Line graph -> sales trend
axes[0, 0].plot(df5["Product"], df5["Sales"], marker="o", color="darkgreen")
axes[0, 0].set_title("Sales Trend")
axes[0, 0].set_ylabel("Sales")

# Bar chart -> product vs sales
axes[0, 1].bar(df5["Product"], df5["Sales"], color="mediumseagreen")
axes[0, 1].set_title("Product vs Sales")
axes[0, 1].set_ylabel("Sales")

# Pie chart -> sales contribution
axes[0, 2].pie(df5["Sales"], labels=df5["Product"], autopct="%1.1f%%")
axes[0, 2].set_title("Sales Contribution")

# Histogram -> profit distribution
axes[1, 0].hist(df5["Profit"], bins=4, color="dodgerblue", edgecolor="black")
axes[1, 0].set_title("Profit Distribution")
axes[1, 0].set_xlabel("Profit")
axes[1, 0].set_ylabel("Frequency")

# Scatter plot -> sales vs profit
axes[1, 1].scatter(df5["Sales"], df5["Profit"], color="purple", s=80)
axes[1, 1].set_title("Sales vs Profit")
axes[1, 1].set_xlabel("Sales")
axes[1, 1].set_ylabel("Profit")

axes[1, 2].axis("off")
plt.tight_layout()
plt.show()
