import sqlite3

def create_db():
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    
    # Create a table for tasks
    c.execute('''CREATE TABLE IF NOT EXISTS tasks
                 (id INTEGER PRIMARY KEY, task TEXT, deadline TEXT, status TEXT)''')
    conn.commit()
    conn.close()

def add_task(task, deadline):
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    
    # Insert a new task
    c.execute("INSERT INTO tasks (task, deadline, status) VALUES (?, ?, ?)", 
              (task, deadline, 'pending'))
    conn.commit()
    conn.close()

def list_tasks():
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    
    # Retrieve all tasks
    c.execute("SELECT * FROM tasks")
    tasks = c.fetchall()
    conn.close()
    return tasks
