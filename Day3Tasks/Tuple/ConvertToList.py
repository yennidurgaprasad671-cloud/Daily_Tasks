#7. Write a program to convert a tuple to a list and modify the element.

t=1,2,3
print(t)
t2=list(t)
t2[1]=4
t3=tuple(t2)
print("After Modifing the tuple ",t3)
