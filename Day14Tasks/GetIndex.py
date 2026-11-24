"""3. Accessing Specific Data (Indexing)
A Series contains:
S = pd.Series([100, 200, 300, 400], index=["A", "B", "C", "D"])
Task:
● Access values for B and D
● Return them as a subse"""
import pandas as pd

S = pd.Series([100, 200, 300, 400], index=["A", "B", "C", "D"])

# Access values for B and D as a subset
subset = S[["B", "D"]]
print(subset)
