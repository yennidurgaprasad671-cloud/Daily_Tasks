"""10. Data Cleaning + Visualization
Scenario:
data = np.array([100, np.nan, 200, 150, np.nan, 300])
Task:
1. Convert to Pandas Series
2. Replace NaN with mean
3. Plot:
○ Line graph of cleaned data
○ Bar chart of values > average """

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


data = np.array([100, np.nan, 200, 150, np.nan, 300])

# 1. Convert to Pandas Series
s = pd.Series(data)

# 2. Replace NaN with mean
mean_val = s.mean()
cleaned_s = s.fillna(mean_val)

# 3. Plot both graphs
fig, axes = plt.subplots(1, 2, figsize=(12, 4))

# Line graph of cleaned data
axes[0].plot(cleaned_s.index, cleaned_s.values, marker="o", color="purple")
axes[0].set_title("Cleaned Data (Line Graph)")
axes[0].set_xlabel("Index")
axes[0].set_ylabel("Values")

# Bar chart of values > average
above_avg = cleaned_s[cleaned_s > mean_val]
axes[1].bar(above_avg.index.astype(str), above_avg.values, color="teal")
axes[1].set_title(f"Values > Average ({mean_val})")
axes[1].set_xlabel("Index")
axes[1].set_ylabel("Values")

plt.tight_layout()
plt.show()
