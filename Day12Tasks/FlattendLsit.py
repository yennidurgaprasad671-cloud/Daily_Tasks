"""6. Multi-Level List Transformation (Advanced List Comprehension)
A dataset contains:
data = [[1, 2, 3], [4, 5], [6]]
Task:
● Flatten the list using list comprehension.
● Then create a new list containing squares of only even numbers."""

data = [[1, 2, 3], [4, 5], [6]]

# Flatten the list
flattened = [num for sublist in data for num in sublist]

# Squares of only even numbers
even_squares = [num ** 2 for num in flattened if num % 2 == 0]

print("Flattened:", flattened)
print("Even squares:", even_squares)
