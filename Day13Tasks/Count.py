"""7. Count Occurrences
You have:
data = np.array([1, 2, 2, 3, 1, 4, 2, 3])
Task:
● Count how many times each unique number appears.
● Return numbers with their counts."""

import numpy as np
data = np.array([1, 2, 2, 3, 1, 4, 2, 3])
unique_nums, counts = np.unique(data, return_counts=True)
result = dict(zip(unique_nums, counts))
print(result)
