#7. Write a program to check whether a key exists in a dictionary.

students = {"Charan":25,"Karthik":23,"Mohan":25,"Manoj":22,"Shourya":25}
print(students)
key=input("Enter Key to Find ")
if key in students:
    print("Key is present in the Dictionary")
else:
    print("Key Not Present in the dictionary ")
