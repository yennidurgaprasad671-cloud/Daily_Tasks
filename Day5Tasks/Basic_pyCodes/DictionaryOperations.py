""" List of Dictionaries: Given the following data:
 
    ```python
    employees = [
        {"name": "John", "age": 25, "salary": 30000},
        {"name": "Alice", "age": 30, "salary": 50000},
        {"name": "Bob", "age": 28, "salary": 40000},
        {"name": "David", "age": 35, "salary": 60000}
    ]
    ```
 
    Perform the following:
 
    * Find the employee with the highest salary.
 
    * Filter employees whose salary is greater than 35,000.
 
    * Calculate the average salary.
 
    * Create a list containing only employee names."""

employees = [
        {"name": "John", "age": 25, "salary": 30000},
        {"name": "Alice", "age": 30, "salary": 50000},
        {"name": "Bob", "age": 28, "salary": 40000},
        {"name": "David", "age": 35, "salary": 60000}
    ]

highest_salary_emp = max(employees, key=lambda emp: emp["salary"])
print("Highest salary employee:", highest_salary_emp["name"])
filtered_emps = [emp for emp in employees if emp["salary"] > 35000]
print( "Salaries > 35,000:", [emp["name"] for emp in filtered_emps])
avg_salary = sum(emp["salary"] for emp in employees) / len(employees)
print("Average salary:", avg_salary)
names_list = [emp["name"] for emp in employees]
print("Employee names:", names_list)
