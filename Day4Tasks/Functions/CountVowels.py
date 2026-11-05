#19. Write a function that takes a string as input and returns the number of vowels.

def number_of_vowels(s):
    s1="aeiouAEIOU"
    count=0
    for char in s:
        if char in s1:
            count+=1
    return count
s=input("Enter a String")
print("Count of Vowels is ", number_of_vowels(s))
