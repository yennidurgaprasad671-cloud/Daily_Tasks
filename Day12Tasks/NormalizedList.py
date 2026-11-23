"""12. Random Dataset Normalization + Filtering
Scenario:
● Generate 8 random float values between 0 and 1.
Task:
1. Normalize by multiplying with 100
2. Filter values greater than 50
3. Sort the filtered values"""

import numpy as np

# Generate 8 random floats between 0 and 1
raw_data = np.random.rand(8)

# 1. Multiply by 100
normalized = raw_data * 100

# 2. Filter values greater than 50
filtered = normalized[normalized > 50]

# 3. Sort the filtered values
sorted_vals = np.sort(filtered)

print("Normalized:", np.round(normalized, 2))
print("Sorted (> 50):", np.round(sorted_vals, 2))
