#Write a program to check whether a number is a Palindrome.

n=int(input("Enter a Number to Find palindrome or Not "))
s=str(n)
s1=s[::-1]
n1=int(s1)
if n==s1:
    print("The Given Number is Palindrome ")
else:
    print("The Nuber is Not Palindrome ")
