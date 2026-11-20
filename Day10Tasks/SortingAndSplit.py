"""10. Data Processing Pipeline
A data pipeline receives the following array:
[12, 7, 25, 3, 18, 10]
Scenario:
1. Convert the list into a NumPy array.
2. Sort the array.
3. Split the sorted array into two equal parts.
4. Calculate the sum of each part.
Output:
● Sorted array
● Two split arrays
● Sum of each part """
import numpy as np

# Input list
data = [12, 7, 25, 3, 18, 10]

# 1. Convert the list into a NumPy array
arr = np.array(data)

# 2. Sort the array
sorted_arr = np.sort(arr)

# 3. Split the sorted array into two equal parts
part1, part2 = np.array_split(sorted_arr, 2)

# 4. Calculate the sum of each part
sum_part1 = np.sum(part1)
sum_part2 = np.sum(part2)

# Output results
print("Sorted array:", sorted_arr)
print("Two split arrays:", part1, "and", part2)
print("Sum of each part:", sum_part1, "and", sum_part2)
