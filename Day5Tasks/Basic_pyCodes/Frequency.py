#Frequency Counter: Given a string `"programming"`, create a dictionary that counts how many times each character appears.
s="programming"
print(s)
f={}
for char in s:
    f[char]=f.get(char,0)+1
print(f)
