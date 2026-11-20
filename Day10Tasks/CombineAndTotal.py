"""9. Multi-Department Data Aggregation
A company collects employee counts from two branches.
Branch A:
[[10, 20],
[30, 40]]
Branch B:
[[5, 15],
[25, 35]]
Scenario:
● Combine the two matrices.
● Calculate the total employees across all departments.
● Print the combined matrix and total"""

import numpy as np

# Define the matrices for Branch A and Branch B
branch_a = np.array([[10, 20], [30, 40]])
branch_b = np.array([[5, 15], [25, 35]])

# 1. Combine the two matrices (element-wise addition)
combined_matrix = branch_a + branch_b

# 2. Calculate the total employees across all departments
total_employees = np.sum(combined_matrix)

# 3. Print the combined matrix and total
print("Combined Matrix:")
print(combined_matrix)
print("Total Employees:", total_employees)
