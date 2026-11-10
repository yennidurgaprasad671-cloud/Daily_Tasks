"""Common Elements Using Sets: Given two lists:
 
    ```python
    list1 = [1, 2, 3, 4, 5]
    list2 = [3, 4, 5, 6, 7]
    ```
 
    Find:
 
    * Common elements.
 
    * Elements present only in the first list.
 
    * All unique elements from both lists."""

l = [1, 2, 3, 4, 5]
l2 = [3, 4, 5, 6, 7]
s=set(l)
s2=set(l2)
print("The Intersction is ", s.intersection(s2))
print("The Elements in first ",s.difference(s2))
print("The elements in unique ",s.union(s2))

