from datetime import datetime

tasks = []

def add_task(task_text):
    task = {
        'text': task_text,
        'created_at': datetime.now(),
        'completed': False
    }
    tasks.append(task)
    return task

def get_last_10_tasks():
    return tasks[-10:]

def get_tasks_for_today():
    today = datetime.now().date()
    return [task for task in tasks if task['created_at'].date() == today]

def mark_task_as_completed(task_index):
    if 0 <= task_index < len(tasks):
        tasks[task_index]['completed'] = True
        return tasks[task_index]
    return None