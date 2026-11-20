"""8. Inventory Update System
A warehouse has an inventory stored in a matrix.
[[10, 15],
[20, 25]]
Scenario:
A new shipment increases every item quantity by 2 units.
Task:
● Add 2 to every element using NumPy.
● Print the updated inventory."""
import numpy as np

a=[[10, 15],[20, 25]]
b= np.array(a)
print(b)
print("After Adding 2 To Every Elemnt ",b+2)
