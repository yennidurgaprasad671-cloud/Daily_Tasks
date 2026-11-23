"""1. Bank Transaction Storage
A bank stores the transaction amounts of a customer in a list:
[1200, 500, 800, 1500]
Scenario:
● Convert the list into a NumPy array.
● Print the type of the object.
● Verify that it is a NumPy ndarray"""

import numpy as np

a=[1200, 500, 800, 1500]
print("Converting to Numpy array")
b=np.array(a)
print(type(b))
is_ndarray = isinstance(b,np.ndarray)
print("The Array ndarray or Not:",is_ndarray)
