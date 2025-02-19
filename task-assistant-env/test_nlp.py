import csv  # Ensure csv is imported here
from nlp_task_parser import NlpTaskParser
from datetime import datetime

# Initialize the parser object
parser = NlpTaskParser()

# Example usage
user_input = "Remind me to finish the report by 2025-02-20"
task, deadline = parser.parse_task_input(user_input)

# Output the parsed task and deadline
print(f"Task: {task}, Deadline: {deadline}")

# Display all tasks from CSV
def display_tasks():
    try:
        with open("tasks.csv", mode="r") as file:
            reader = csv.reader(file)  # Create a CSV reader object
            next(reader)  # Skip header row
            print("\nAll tasks in the system:")
            for row in reader:
                task, deadline, created_at = row
                print(f"Task: {task}, Deadline: {deadline}, Created At: {created_at}")
    except FileNotFoundError:
        print("No tasks found.")

# Call the function to display tasks from the CSV
display_tasks()

# Reminder system for tasks due soon
def check_and_send_reminders():
    try:
        with open("tasks.csv", mode="r") as file:
            reader = csv.reader(file)  # Create a CSV reader object
            next(reader)  # Skip header row
            for row in reader:
                task, deadline, _ = row
                deadline_date = datetime.strptime(deadline, "%Y-%m-%d")
                current_date = datetime.now()
                # Check if the deadline is within the next day
                if (deadline_date - current_date).days <= 1:
                    print(f"Reminder: You have a task '{task}' with a deadline of {deadline}.")
    except FileNotFoundError:
        print("No tasks found.")

# Check for reminders
check_and_send_reminders()
