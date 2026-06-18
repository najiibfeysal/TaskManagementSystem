from task_manager.validation import (
    validate_task_title,
    validate_task_description,
    validate_due_date
)


def add_task(tasks, title, description, due_date):

    validate_task_title(title)
    validate_task_description(description)
    validate_due_date(due_date)

    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    }

    tasks.append(task)

    print("Task added successfully!")


def mark_task_as_complete(tasks, title):

    for task in tasks:
        if task["title"].lower() == title.lower():
            task["completed"] = True
            print("Task marked as complete!")
            return

    print("Task not found.")


def view_pending_tasks(tasks):

    pending = [task for task in tasks if not task["completed"]]

    if not pending:
        print("No pending tasks.")
        return

    for task in pending:
        print(
            f"{task['title']} | "
            f"{task['description']} | "
            f"{task['due_date']}"
        )


def calculate_progress(tasks):

    if len(tasks) == 0:
        return 0

    completed = sum(
        1 for task in tasks
        if task["completed"]
    )

    return (completed / len(tasks)) * 100