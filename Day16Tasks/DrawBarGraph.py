"""5. Product Sales Bar Chart
Scenario:
products = ["Pen", "Book", "Pencil"]
sales = np.array([50, 80, 40])
Task:
● Create DataFrame
● Plot bar chart
● Add labels and title """

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
products = ["Pen", "Book", "Pencil"]
sales = np.array([50, 80, 40])

df = pd.DataFrame({"Products": products, "Sales": sales})

plt.bar(df["Products"], df["Sales"], color="orange")
plt.xlabel("Products")
plt.ylabel("Sales")
plt.title("Product Sales")
plt.show()
