#5. Write a program to assign grades based on marks (for example: A, B, C, Fail).

a=int(input("Enter Your Marks"))
print("Grade Assigning After Your Marks ")
if a>=90 and a<=100:
    print(" A")
elif a>=70:
    print("B")
elif a>=35:
    print("c")
else:
    print("Fail")
