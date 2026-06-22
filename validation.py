from datetime import datetime


def validate_task(title, description, due_date):
    if not isinstance(title, str):
        raise ValueError("Title must be a string")
    if len(title) == 0:
        raise ValueError("Title cannot be empty")

    if not isinstance(description, str):
        raise ValueError("Description must be a string")
    if len(description) == 0:
        raise ValueError("Description cannot be empty")

    if not isinstance(due_date, str):
        raise ValueError("Due date must be a string")
    if len(due_date) == 0:
        raise ValueError("Due date cannot be empty")

    try:
        datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Due date must be in YYYY-MM-DD format")

    return True


def validate_task_title(title):
    if len(title) == 0:
        raise ValueError("Title cannot be empty")
    return True


def validate_task_description(description):
    if len(description) == 0:
        raise ValueError("Description cannot be empty")
    return True


def validate_due_date(due_date):
    if len(due_date) == 0:
        raise ValueError("Due date cannot be empty")
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Due date must be in YYYY-MM-DD format")
    return True
