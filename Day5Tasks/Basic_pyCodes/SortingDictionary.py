"""* Dictionary Sorting: Given a dictionary:
 
    ```python
    students = {
        "Rahul": 85,
        "Amit": 92,
        "Priya": 78,
        "Sneha": 95
    }
    ```
 
    Sort the dictionary based on marks in descending order and print the top two students."""


students = {"Rahul": 85, "Amit": 92, "Priya": 78, "Sneha": 95}
sorted_students = sorted(students.items(), key=lambda x: x[1], reverse=True)
print("Top two students:")
for name, marks in sorted_students[:2]:
  print(f"{name}: {marks}")
