"""7. Generator-based Log Reader
Scenario:
A large log file needs to be processed.
Task:
● Create a generator to read file line by line
● Use loop to process logs
● Use condition to filter errors
● Count occurrences using a dictionary """

# Create a sample log file for demonstration
with open("server.log", "w") as f:
  f.write(
      "INFO: Server started\n"
      "ERROR: Database timeout\n"
      "WARNING: High memory usage\n"
      "ERROR: File not found\n"
      "ERROR: Database timeout\n"
  )


# Generator to read file line by line
def read_logs(file_path):
  with open(file_path, "r") as file:
    for line in file:
      yield line.strip()


error_counts = {}

# Use loop to process logs and condition to filter errors
for log_line in read_logs("server.log"):
  if log_line.startswith("ERROR:"):
    error_msg = log_line.replace("ERROR:", "").strip()
    error_counts[error_msg] = error_counts.get(error_msg, 0) + 1

print("Error Occurrences:", error_counts)
