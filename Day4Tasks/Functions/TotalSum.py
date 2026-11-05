#18. Write a function to find the sum of elements in a list using a user-defined function

def total(l):
    sum=0
    for i in l:
        sum+=i
    return sum
l=[1,2,3,4,5]
print(l)
print("The Toal Sum in the list is ", total(l))
