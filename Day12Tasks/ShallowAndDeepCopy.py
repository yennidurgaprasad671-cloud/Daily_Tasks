"""3. Employee Data Copy Issue (Shallow vs Deep Copy)
A company stores employee data:
employees = [[101, "A"], [102, "B"], [103, "C"]]
Scenario:
● Create a shallow copy of the list.
● Modify one nested list (e.g., change "A" to "Z").
● Observe changes in both lists.
Task:
● Explain why the change reflects in both.
● Fix it using deep copy."""

import copy

employees = [[101, "A"], [102, "B"], [103, "C"]]
shallow_emp = employees.copy()
shallow_emp[0][1] = "Z"

print("Original after shallow copy change:", employees)
print("Shallow copy:", shallow_emp)

# 2. Fix using deep copy
employees = [[101, "A"], [102, "B"], [103, "C"]]
deep_emp = copy.deepcopy(employees)
deep_emp[0][1] = "Z"

print("\nOriginal after deep copy change:", employees)
print("Deep copy:", deep_emp)
