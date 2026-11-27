"""6. Student Marks Analysis (NumPy → Pandas)
Marks data:
arr = np.array([
[80, 90],
[70, 60],
[85, 95]
])
Task:
● Convert into DataFrame with columns "Math", "Science"
● Add a new column Total
● Find student with highest total"""

import pandas as pd
import numpy as np

arr = np.array([
[80, 90],
[70, 60],
[85, 95]
])
col =["Math","Science"]

s = pd.DataFrame(arr,columns=col)
print(s)
s["Total"] = s["Math"]+s["Science"]
print(s)
