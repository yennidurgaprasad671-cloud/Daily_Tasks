"""9. Combined Visualization Dashboard
Scenario:
sales = np.array([100, 200, 150, 300])
products = ["A", "B", "C", "D"]
Task:
● Create DataFrame
● Plot:
○ Line graph (trend)
○ Bar chart (comparison)
○ Pie chart (distribution)
● Show all in single figure (subplots)
"""
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

sales = np.array([100, 200, 150, 300])
products = ["A", "B", "C", "D"]

df = pd.DataFrame({"Products": products, "Sales": sales})

fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# 1. Line graph (trend)
axes[0].plot(df["Products"], df["Sales"], marker="o", color="blue")
axes[0].set_title("Sales Trend")
axes[0].set_xlabel("Products")
axes[0].set_ylabel("Sales")

# 2. Bar chart (comparison)
axes[1].bar(df["Products"], df["Sales"], color="coral")
axes[1].set_title("Sales Comparison")
axes[1].set_xlabel("Products")
axes[1].set_ylabel("Sales")

# 3. Pie chart (distribution)
axes[2].pie(df["Sales"], labels=df["Products"], autopct="%1.1f%%")
axes[2].set_title("Sales Distribution")

plt.tight_layout()
plt.show()
