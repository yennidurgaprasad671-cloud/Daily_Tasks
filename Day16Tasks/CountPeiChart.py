"""8. Pie Chart with Conditional Data
Scenario:
scores = np.array([40, 60, 80, 30, 90])
Task:
● Categorize into:
○ Pass (>50)
○ Fail (<=50)
● Count using NumPy/Pandas
● Plot pie chart for Pass vs Fail
"""

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

scores = np.array([40, 60, 80, 30, 90])
cat = pd.Series(np.where(scores >50, "Pass" , "Fails"))
counts = cat.value_counts()
plt.pie(counts,labels =counts.index, autopct ="%1.1f%%", startangle=90)
plt.show()
