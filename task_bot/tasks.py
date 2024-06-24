import json
import os
from datetime import datetime

TASKS_FILE = 'tasks.json'

if not os.path.exists(TASKS_FILE):
    with open(TASKS_FILE, 'w') as f:
        json.dump({}, f)

def load_tasks():
    with open(TASKS_FILE, 'r') as f:
        return json.load(f)

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, ensure_ascii=False, indent=4)

def add_task(user_id, description):
    tasks = load_tasks()
    if str(user_id) not in tasks:
        tasks[str(user_id)] = []
    task = {
        'description': description,
        'date': str(datetime.now().date()),
        'done': False
    }
    tasks[str(user_id)].append(task)
    save_tasks(tasks)

def get_last_tasks(user_id, n=10):
    tasks = load_tasks()
    print(user_id in tasks)
    print(user_id)
    print(tasks)
    if str(user_id) in tasks:
        return tasks[str(user_id)][-n:]
    return []

def get_today_tasks(user_id):
    tasks = load_tasks()
    if str(user_id) in tasks:
        today = str(datetime.now().date())
        return [task for task in tasks[str(user_id)] if task['date'] == today]
    return []

def mark_task_done(user_id, task_name):
    tasks = load_tasks()
    change = False
    if str(user_id) in tasks:
        for i in range(0, len(tasks[str(user_id)])):
            if tasks[str(user_id)][i]["description"] == task_name:
                change = True
                tasks[str(user_id)][i]['done'] = True
        save_tasks(tasks)
    return change
