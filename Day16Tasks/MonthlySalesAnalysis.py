"""2. Monthly Sales Analysis
Scenario:
sales = np.array([100, 150, 200, 180, 220, 300])
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
Task:
● Create DataFrame
● Plot:
○ Line graph → sales trend
○ Bar chart → month-wise comparison
○ Pie chart → contribution of each month
○ Histogram → frequency of sales values
○ Scatter plot → month index vs sales
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Data
sales = np.array([100, 150, 200, 180, 220, 300])
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

# 1. Create DataFrame
df2 = pd.DataFrame({"Month": months, "Sales": sales})

# Plotting
fig, axes = plt.subplots(2, 3, figsize=(15, 8))
fig.suptitle("2. Monthly Sales Analysis", fontsize=16, fontweight="bold")

# Line graph -> sales trend
axes[0, 0].plot(df2["Month"], df2["Sales"], marker="o", color="green")
axes[0, 0].set_title("Sales Trend")
axes[0, 0].set_ylabel("Sales")

# Bar chart -> month-wise comparison
axes[0, 1].bar(df2["Month"], df2["Sales"], color="orange")
axes[0, 1].set_title("Month-wise Comparison")
axes[0, 1].set_ylabel("Sales")

# Pie chart -> contribution of each month
axes[0, 2].pie(df2["Sales"], labels=df2["Month"], autopct="%1.1f%%")
axes[0, 2].set_title("Contribution of Each Month")

# Histogram -> frequency of sales values
axes[1, 0].hist(df2["Sales"], bins=4, color="teal", edgecolor="black")
axes[1, 0].set_title("Frequency of Sales Values")
axes[1, 0].set_xlabel("Sales")
axes[1, 0].set_ylabel("Frequency")

# Scatter plot -> month index vs sales
axes[1, 1].scatter(df2.index, df2["Sales"], color="darkorange")
axes[1, 1].set_title("Month Index vs Sales")
axes[1, 1].set_xlabel("Month Index")
axes[1, 1].set_ylabel("Sales")

axes[1, 2].axis("off")
plt.tight_layout()
plt.show()
