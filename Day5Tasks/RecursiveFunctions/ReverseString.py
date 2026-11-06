#4. Write a recursive function to reverse a string.

def reverse(s):
    if len(s)==0:
        return s
    return reverse(s[1:])+s[0]
s=input("Enter  String To Reverse ")
print("The Reversed String is ", reverse(s))
