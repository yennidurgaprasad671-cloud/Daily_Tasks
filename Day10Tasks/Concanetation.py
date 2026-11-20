"""4. Combine Two Sensor Readings
Two sensors record readings during a test.
Scenario:
Sensor1 = [10, 20, 30]
Sensor2 = [40, 50, 60]
Task:
● Store both readings in NumPy arrays.
● Combine them into one array using NumPy concatenation"""
import numpy as np
s1 = [10, 20, 30]
s2 = [40, 50, 60]
print(s1,s2)
a=np.array(s1)
b=np.array(s2)
print("After combining")
print(np.concatenate((a,b)))
