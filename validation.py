from datetime import datetime


def validate_task_title(title):
    if not isinstance(title, str):
        raise ValueError("Task title must be a non-empty string.")

    title = title.strip()
    if len(title) == 0:
        raise ValueError("Task title must be a non-empty string.")
    if len(title) > 100:
        raise ValueError("Task title must be 100 characters or fewer.")
    return True


def validate_task_description(description):
    if not isinstance(description, str):
        raise ValueError("Task description must be a non-empty string.")

    description = description.strip()
    if len(description) == 0:
        raise ValueError("Task description must be a non-empty string.")
    if len(description) > 255:
        raise ValueError("Task description must be 255 characters or fewer.")
    return True


def validate_due_date(due_date):
    if not isinstance(due_date, str):
        raise ValueError("Due date must be a non-empty string in YYYY-MM-DD format.")

    due_date = due_date.strip()
    if len(due_date) == 0:
        raise ValueError("Due date must be a non-empty string in YYYY-MM-DD format.")

    try:
        datetime.strptime(due_date, "%Y-%m-%d")
        return True
    except ValueError:
        raise ValueError("Due date must be in YYYY-MM-DD format.")
