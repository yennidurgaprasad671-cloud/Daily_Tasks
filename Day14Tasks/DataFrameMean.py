"""10. Row Filtering + Aggregation
A dataset:
arr = np.array([
[100, 200],
[150, 250],
[80, 120],
[300, 400]
])
Task:
● Convert to DataFrame with columns "Sales", "Profit"
● Filter rows where Sales > 100
● Find average Profit of filtered rows"""

import pandas as pd
import numpy as np

arr = np.array([
[100, 200],
[150, 250],
[80, 120],
[300, 400]
])

d = pd.DataFrame(arr,columns=["Sales","Profit"])
print(d)
d2= d[d["Sales"]>100]
print(d2)
average = d2["Profit"].mean()
print(average)
