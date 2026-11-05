#10. Write a program to remove duplicate characters from a string.

s=input("Enter a String ")
s1=""
for char in s:
    if char not in s1:
        s1+=char
print(s1)
