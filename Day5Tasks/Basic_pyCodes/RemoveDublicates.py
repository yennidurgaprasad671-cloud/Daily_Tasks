#Remove Duplicates: Given a list `[1, 2, 3, 2, 4, 1, 5, 3]`, remove duplicate elements while preserving the original order. Do not use `set()`.
l=[1, 2, 3, 2, 4, 1, 5, 3]
print(l)
l2=[]
for i in l:
    if i not in l2:
        l2.append(i)
print(l2)

