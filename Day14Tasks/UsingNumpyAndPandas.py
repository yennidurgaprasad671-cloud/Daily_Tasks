"""1. Convert NumPy Array to Pandas Series
A dataset:
arr = np.array([10, 20, 30, 40])
Task:
● Convert this NumPy array into a Pandas Series
● Assign index labels: ["A", "B", "C", "D"] """
import pandas as pd
import numpy as np

arr = np.array([10, 20, 30, 40])
labels=["A", "B", "C", "D"]
arr1 = pd.Series(arr,index=labels)
print(arr1)
