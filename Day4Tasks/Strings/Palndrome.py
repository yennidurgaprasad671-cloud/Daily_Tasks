#8. Write a program to check whether a string is a palindrome.

s=input("Enter a String ")
print(s)
s1=s.lower()
if s1==s1[::-1]:
    print("Enter String is Palindrome ")
else:
    print("Not Palindrome")
