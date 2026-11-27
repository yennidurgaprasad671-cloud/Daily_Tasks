"""3. Expense Distribution Pie Chart
Scenario:
Monthly expenses:
expenses = np.array([500, 300, 200])
labels = ["Food", "Rent", "Travel"]
"""
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

expenses = np.array([500, 300, 200])
labels = ["Food", "Rent", "Travel"]

plt.pie(expenses, labels=labels, autopct="%1.1f%%", startangle=90)
plt.title("Expense Distribution")
plt.show()
