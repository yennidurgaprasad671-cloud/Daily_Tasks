#3. Write a program to access the second element in a tuple

t=1,2,5,6,7,8,4,3
t2=list(t)
t2.sort()
print(t)
print("The Second Largest Elemet is",t2[len(t)-2])
