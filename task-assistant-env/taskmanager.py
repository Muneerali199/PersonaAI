# task_manager.py
from database import add_task, list_tasks

# Add a task to the database
add_task("Finish the report", "2025-02-20")

# List all tasks in the database
tasks = list_tasks()
for task in tasks:
    print(f"Task ID: {task[0]}, Description: {task[1]}, Deadline: {task[2]}, Status: {task[3]}")
