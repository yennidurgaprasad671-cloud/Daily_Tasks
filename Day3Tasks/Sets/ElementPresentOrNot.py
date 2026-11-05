#4. Write a program to check if an element exists in a set.

s={1,2,3,4,5,6}
print("Elements In the set are", s)
n=int(input("Enter Element to Find "))
if n in s:
    print("Element Present in Set")
else:
    print("Element Not in The Set ")
    
