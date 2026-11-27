"""9. Smart Data Processing Pipeline
Scenario:
A system processes numeric data from file.
Task:
● Read numbers from a file
● Use NumPy for calculations (mean, std)
● Convert results to Pandas DataFrame
● Use exception handling for bad data
● Use a generator to stream data
● Apply decorator to measure execution time
"""
from functools import wraps
import time
import numpy as np
import pandas as pd

# Create sample numeric file with one bad entry
with open("numbers.txt", "w") as f:
  f.write("12.5\n45.0\ninvalid_num\n33.2\n18.8\n29.5\n")


# Decorator to measure execution time
def measure_time(func):

  @wraps(func)
  def wrapper(*args, **kwargs):
    start = time.perf_counter()
    result = func(*args, **kwargs)
    elapsed = time.perf_counter() - start
    print(f"Execution time for '{func.__name__}': {elapsed:.6f} seconds")
    return result

  return wrapper


# Generator to stream valid numbers from file
def stream_numbers(file_path):
  with open(file_path, "r") as file:
    for line_num, line in enumerate(file, 1):
      try:
        yield float(line.strip())
      except ValueError:
        print(f"Skipping bad data on line {line_num}: '{line.strip()}'")


@measure_time
def process_pipeline(file_path):
  data = np.array(list(stream_numbers(file_path)))

  mean_val = np.mean(data)
  std_val = np.std(data)

  summary_df = pd.DataFrame(
      {"Metric": ["Count", "Mean", "Standard Deviation"], "Value": [len(data), mean_val, std_val]}
  )
  return summary_df


result_df = process_pipeline("numbers.txt")
print("\n", result_df)
