"""7. Data Alignment Issue in Series Addition
Two Series:
S1 = pd.Series([10, 20, 30], index=["a", "b", "c"])
S2 = pd.Series([5, 15, 25], index=["b", "c", "d"])
Task:
● Add both Series
● Explain why some values become NaN
● Replace NaN with 0 and compute final result"""

import pandas as pd

s1 = pd.Series([10, 20, 30], index=["a", "b", "c"])
s2 = pd.Series([5, 15, 25], index=["b", "c", "d"])

s3= s1+s2
print(s3)

final_result = s1.add(s2, fill_value=0)
print(final_result)
