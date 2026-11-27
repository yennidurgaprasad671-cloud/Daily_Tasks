"""1. Student Score Processor
Scenario:
A teacher stores student names and marks in a list of tuples.
Task:
● Convert data into a dictionary
● Use a loop + condition to find students scoring above 50
● Use math module to calculate average
● Store results in a text file """

import math

# Sample data: list of tuples (student_name, mark)
student_scores = [
    ("Aarav", 88),
    ("Diya", 45),
    ("Rohan", 72),
    ("Meera", 91),
    ("Kabir", 39),
    ("Ananya", 64),
]

# 1. Convert list of tuples into a dictionary
scores_dict = dict(student_scores)

# 2. Use a loop + condition to find students scoring above 50
passed_students = {}
for name, score in scores_dict.items():
  if score > 50:
    passed_students[name] = score

# 3. Use math module to calculate average
# math.fsum() provides an accurate floating-point sum of values
total_marks = math.fsum(scores_dict.values())
average_score = total_marks / len(scores_dict)

# 4. Store results in a text file
output_filename = "student_results.txt"

with open(output_filename, "w") as file:
  file.write("=== Student Score Report ===\n\n")
  file.write(f"Class Average: {average_score:.2f}\n")
  file.write(f"Rounded Up Average (math.ceil): {math.ceil(average_score)}\n\n")

  file.write("Students Scoring Above 50:\n")
  for name, score in passed_students.items():
    file.write(f"- {name}: {score}\n")

print(f"Processing complete. Results saved to '{output_filename}'.")
