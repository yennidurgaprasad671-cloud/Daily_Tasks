"""2. Write a program that uses random.choice() to randomly select a student from a
list and display:
"The selected student for presentation is: <name>"."""

from random import *
l=["Prasad","Manoj","Charan","Karthik","Mohan"]
print(l)
print("The Selected Student for presentation is: ",choice(l))

