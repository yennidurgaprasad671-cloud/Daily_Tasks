#8. Write a program to find the student with the highest marks from a dictionary.

students = {"Charan":100,"Karthik":80,"Mohan":90,"Manoj":80,"Shourya":200}
print(students)
highest_student=max(students,key=students.get)
print("highest marks of the students key is ",highest_student)
print("Marks are ",students[highest_student])

