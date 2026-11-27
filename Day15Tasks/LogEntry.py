"""4. Basic File Logger
Scenario:
A system logs user actions.
Task:
● Take user input
● Store logs in a file
● Use loop to allow multiple entries
● Handle file errors using exception handling """

from datetime import datetime

log_file = "system_actions.log"

print("Enter user actions to log (type 'exit' to quit):")

while True:
  action = input("Action: ").strip()
  if action.lower() == "exit":
    break
  if not action:
    continue

  timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  log_entry = f"[{timestamp}] USER_ACTION: {action}\n"

  try:
    with open(log_file, "a") as file:
      file.write(log_entry)
    print("Logged successfully.")
  except (IOError, PermissionError) as e:
    print(f"File error while writing log: {e}")
