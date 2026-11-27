"""10. Advanced Simulation System
Scenario:
Simulate exam results and generate reports.
Task:
● Generate random marks using random
● Store in NumPy array
● Convert to Pandas DataFrame
● Use OOP to represent Student
● Use conditions + loops to assign grades
● Save report to file
● Handle errors using try-except
● Use math module for statistic"""
import math
import random
import numpy as np
import pandas as pd


class Student:

  def __init__(self, student_id, name, mark):
    self.student_id = student_id
    self.name = name
    self.mark = mark
    self.grade = self.assign_grade()

  def assign_grade(self):
    if self.mark >= 90:
      return "A"
    elif self.mark >= 75:
      return "B"
    elif self.mark >= 60:
      return "C"
    elif self.mark >= 50:
      return "D"
    else:
      return "F"


try:
  num_students = 8
  # Generate random marks using random and store in NumPy array
  raw_marks = [random.randint(35, 100) for _ in range(num_students)]
  marks_array = np.array(raw_marks)

  # Create Student objects using loop
  students = []
  for idx, mark in enumerate(marks_array, start=1):
    students.append(Student(f"S0{idx}", f"Student_{idx}", int(mark)))

  # Convert to Pandas DataFrame
  df = pd.DataFrame([
      {"ID": s.student_id, "Name": s.name, "Mark": s.mark, "Grade": s.grade}
      for s in students
  ])

  # Calculate statistics using math module
  total = math.fsum(marks_array)
  mean_score = total / len(marks_array)
  variance = math.fsum((x - mean_score) ** 2 for x in marks_array) / len(marks_array)
  std_dev = math.sqrt(variance)

  # Save report to file
  report_file = "exam_simulation_report.txt"
  with open(report_file, "w") as file:
    file.write("=== Exam Simulation Report ===\n\n")
    file.write(df.to_string(index=False))
    file.write(f"\n\nMean Score: {mean_score:.2f}")
    file.write(f"\nStandard Deviation: {std_dev:.2f}\n")

  print(df)
  print(f"\nReport saved successfully to '{report_file}'.")

except Exception as e:
  print(f"An error occurred during simulation: {e}")
