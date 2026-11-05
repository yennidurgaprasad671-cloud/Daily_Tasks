#6. Write a program to count the number of vowels in a string.

s=input("Enter a string ")
print(s)
s1="aeiouAEIOU"
count=0
for char in s:
    if char in s1:
        count+=1
print( "VowerCount is ", count)

        
