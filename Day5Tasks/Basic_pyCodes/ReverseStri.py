#* String Reversal: Write a program to reverse a string without using built-in reverse functions.


def reverse(s):
    i=len(s)
    if i==0:
        return s
    else:
        return reverse(s[1:])+s[0]
s=input(" Enter a String to Reverse ")
print("Reverse String is ", reverse(s))

        
