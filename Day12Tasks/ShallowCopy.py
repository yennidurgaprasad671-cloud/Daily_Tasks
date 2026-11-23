"""1. Student List Backup (Shallow Copy)
A teacher has a list of student marks:
marks = [50, 60, 70, 80]
Scenario:
She creates a backup using assignment:
backup = marks
Task:
● Modify the first element in marks.
● Observe the change in backup.
● Explain why both lists are affected."""
marks = [50, 60, 70, 80]
backup = marks

# Modify the first element in marks
marks[0] = 95

print("marks:", marks)
print("backup:", backup)

#Using backup = marks does not create a new list.
#Both variables point to the exact same list object in memory, so modifying one affects the other.
