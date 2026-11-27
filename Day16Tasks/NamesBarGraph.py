"""2. Student Marks Bar Chart
Scenario:
Marks of students:
names = ["A", "B", "C", "D"]
marks = np.array([70, 85, 60, 90])
Task:
● Create a DataFrame
● Plot a bar graph
● Show student names on X-axis """

import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

names = ["A", "B", "C", "D"]
marks = np.array([70, 85, 60, 90])
df = pd.DataFrame({"Names":names ,"Marks":marks})
plt.bar(df["Names"],df["Marks"],color ="Skyblue")
plt.xlabel("Names")
plt.show()

