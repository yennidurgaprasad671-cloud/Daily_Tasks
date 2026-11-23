"""8. Random Sales Simulation
Scenario:
A company wants to simulate 10 days of sales (range 100–500).
Task:
● Generate random integers using NumPy.
● Print the array.
● Find the average sale"""

import numpy as np

# Generate 10 random integers between 100 and 500 (inclusive)
sales = np.random.randint(100, 501, size=10)
avg_sales = np.mean(sales)

print("10-Day Sales:", sales)
print("Average Sales:", avg_sales)
