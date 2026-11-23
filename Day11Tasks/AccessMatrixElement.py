"""5. Accessing Matrix Data
A teacher stores marks of students in two subjects:
[[78, 85],
[90, 88],
[67, 72]]
Task:
● Convert it to a NumPy array.
● Access the second student's second subject mark"""

import numpy as np

marks = np.array([[78, 85], [90, 88], [67, 72]])
# Second student is at row index 1, second subject is at column index 1
print("Second student's second subject mark:", marks[1, 1])
