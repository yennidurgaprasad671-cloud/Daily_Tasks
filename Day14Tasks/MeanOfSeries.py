"""9. Missing Data Handling (NumPy + Pandas)
A dataset:
arr = np.array([10, np.nan, 30, np.nan, 50])
Task:
● Convert to Pandas Series
● Replace NaN values with the mean of the Series
● Print updated data
"""
import pandas as pd
import numpy as np

arr = np.array([10, np.nan, 30, np.nan, 50])
arr1 =pd.Series(arr)
series= pd.Series(np.where(arr1.isna(),arr1.mean(),arr1))
print(series)
