#. Write a program that searches for a number in a list and breaks the loop when found.

List =[2,3,4,6,7,8,8,9,10]
num=int(input("Enter a number to find"))
for i in List:
    if i==num:
        break
    print("Number is Found in the List")

