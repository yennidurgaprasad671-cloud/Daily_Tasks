"""4. Temperature Trend Line Plot
Scenario:
Daily temperatures:
temps = np.array([28, 30, 32, 31, 29])
Task:
● Convert into Pandas Series
● Plot a line graph
● Add title and grid """

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

temps = np.array([28, 30, 32, 31, 29])

s = pd.Series(temps, index=["Day 1", "Day 2", "Day 3", "Day 4", "Day 5"])

s.plot(kind="line", marker="o")
plt.title("Daily Temperature Trend")
plt.xlabel("Days")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.show()
