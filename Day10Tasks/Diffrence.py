"""5. Store Sales Comparison
Two stores record daily sales for 3 days.
Scenario:
Store A = [200, 250, 300]
Store B = [180, 270, 310]
Task:
● Store them in NumPy arrays.
● Find the daily difference in sales between the two stores.
● Print the resulting array."""

import numpy as np

a = [200, 250, 300]
b = [180, 270, 310]
c=np.array(a)
d=np.array(b)
print("The Resulting Array ",c-d)




