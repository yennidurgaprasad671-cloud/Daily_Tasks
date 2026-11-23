"""10. Random Matrix and Condition Filtering
Scenario:
● Generate a 3×3 matrix of random numbers (0–50).
Task:
● Filter elements greater than 25.
● Print filtered values."""

import numpy as np

# Generate 3x3 matrix with values from 0 to 50
matrix = np.random.randint(0, 51, size=(3, 3))
filtered_vals = matrix[matrix > 25]

print("3x3 Matrix:\n", matrix)
print("Values greater than 25:", filtered_vals)
