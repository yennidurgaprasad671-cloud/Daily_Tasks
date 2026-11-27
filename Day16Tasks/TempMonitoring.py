"""4. Temperature Monitoring System
Scenario:
temps = np.array([28, 30, 32, 35, 33, 31, 29])
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
Task:
● Create DataFrame
● Plot:
○ Line graph → daily temperature trend
○ Bar chart → day-wise temperature
○ Pie chart → proportion of high (>30) vs low temps
○ Histogram → temperature frequency
○ Scatter plot → day index vs temperature"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Data
temps = np.array([28, 30, 32, 35, 33, 31, 29])
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

# 1. Create DataFrame
df4 = pd.DataFrame({"Day": days, "Temp": temps})
df4["Temp_Level"] = np.where(
    df4["Temp"] > 30, "High (>30)", "Low/Normal (<=30)"
)

# Plotting
fig, axes = plt.subplots(2, 3, figsize=(15, 8))
fig.suptitle("4. Temperature Monitoring System", fontsize=16, fontweight="bold")

# Line graph -> daily temperature trend
axes[0, 0].plot(df4["Day"], df4["Temp"], marker="s", color="red")
axes[0, 0].set_title("Daily Temperature Trend")
axes[0, 0].set_ylabel("Temperature (°C)")

# Bar chart -> day-wise temperature
axes[0, 1].bar(df4["Day"], df4["Temp"], color="gold")
axes[0, 1].set_title("Day-wise Temperature")
axes[0, 1].set_ylabel("Temperature (°C)")

# Pie chart -> proportion of high (>30) vs low temps
temp_counts = df4["Temp_Level"].value_counts()
axes[0, 2].pie(
    temp_counts,
    labels=temp_counts.index,
    autopct="%1.1f%%",
    colors=["tomato", "lightskyblue"],
)
axes[0, 2].set_title("High (>30) vs Low Temps")

# Histogram -> temperature frequency
axes[1, 0].hist(df4["Temp"], bins=4, color="coral", edgecolor="black")
axes[1, 0].set_title("Temperature Frequency")
axes[1, 0].set_xlabel("Temperature (°C)")
axes[1, 0].set_ylabel("Frequency")

# Scatter plot -> day index vs temperature
axes[1, 1].scatter(df4.index, df4["Temp"], color="darkred")
axes[1, 1].set_title("Day Index vs Temperature")
axes[1, 1].set_xlabel("Day Index")
axes[1, 1].set_ylabel("Temperature (°C)")

axes[1, 2].axis("off")
plt.tight_layout()
plt.show()
