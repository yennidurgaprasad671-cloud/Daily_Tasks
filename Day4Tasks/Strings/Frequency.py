#9. Write a program to count the frequency of each character in a strings

s=input("Enter a String ")
freq ={}
for char in s:
    if char in freq:
        freq[char]+=1
    else:
        freq[char]=1
print(freq)
