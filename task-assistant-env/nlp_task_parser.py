import spacy
import re
import csv  # Ensure csv is imported here
from datetime import datetime

class NlpTaskParser:
    def __init__(self):
        # Load spaCy's small English model when the class is instantiated
        self.nlp = spacy.load("en_core_web_sm")

    def parse_task_input(self, user_input):
        """
        Parses the input string to extract the task description and deadline.

        :param user_input: The string input from the user.
        :return: A tuple (task, deadline) where task is the task description and 
                 deadline is the extracted date in 'YYYY-MM-DD' format.
        """
        doc = self.nlp(user_input)  # Process the text with spaCy

        task = ""  # To hold the task description
        deadline = None  # To hold the deadline date

        # Use regex to find the date in the sentence (YYYY-MM-DD format)
        date_match = re.search(r'\d{4}-\d{2}-\d{2}', user_input)
        
        if date_match:
            deadline = date_match.group(0)  # Extract the date from the sentence

        # If no date was found, set a default deadline
        if not deadline:
            deadline = "No deadline specified"

        # Loop through the tokens and capture everything except the date
        for token in doc:
            # If the token is a date, skip it
            if token.ent_type_ == "DATE":
                continue
            task += token.text + " "  # Otherwise, treat the token as part of the task description

        task = task.strip()  # Clean up extra spaces around the task description
        self.save_task_to_csv(task, deadline)
        return task, deadline

    def save_task_to_csv(self, task, deadline):
        # Check if the CSV file exists, if not, create it with headers
        file_exists = False
        try:
            with open("tasks.csv", mode="r"):
                file_exists = True
        except FileNotFoundError:
            pass

        # Open the CSV file in append mode
        with open("tasks.csv", mode="a", newline="") as file:
            writer = csv.writer(file)  # Create a CSV writer object
            if not file_exists:
                writer.writerow(["Task", "Deadline", "Date Created"])  # Write header if file is new
            writer.writerow([task, deadline, datetime.now().strftime("%Y-%m-%d %H:%M:%S")])  # Save task with timestamp

# Example usage (in `test_nlp.py`)
