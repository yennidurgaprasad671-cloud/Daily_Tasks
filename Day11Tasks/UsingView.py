"""13. Copy vs View Behavior in Data Processing
Scenario:
A dataset:
[10, 20, 30, 40]
Task:
● Create a copy of the array.
● Modify the original array.
● Show that the copy does not change.
● Repeat using view() and observe the difference."""

import numpy as np

# Using copy()
original = np.array([10, 20, 30, 40])
arr_copy = original.copy()
original[0] = 99
print("Original after modifying:", original)
print("Copy (unchanged):", arr_copy)

# Using view()
original = np.array([10, 20, 30, 40])
arr_view = original.view()
original[0] = 99
print("\nOriginal after modifying:", original)
print("View (reflects changes):", arr_view)
