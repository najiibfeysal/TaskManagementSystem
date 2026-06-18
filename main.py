from task_manager.task_utils import add_task, mark_task_as_complete, view_pending_tasks, calculate_progress


def display_menu():
    print("\nTask Management System")
    print("1. Add a task")
    print("2. Mark a task as complete")
    print("3. View pending tasks")
    print("4. View all tasks")
    print("5. Show progress")
    print("6. Exit")


def display_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return

    for index, task in enumerate(tasks, start=1):
        status = "Completed" if task.get("completed") else "Pending"
        print(f"{index}. {task['title']} ({status})")
        print(f"   Description: {task['description']}")
        print(f"   Due date: {task['due_date']}")


def prompt_for_task_details():
    title = input("Enter task title: ").strip()
    description = input("Enter task description: ").strip()
    due_date = input("Enter due date (YYYY-MM-DD): ").strip()
    return title, description, due_date


def main():
    tasks = []

    while True:
        display_menu()
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            title, description, due_date = prompt_for_task_details()
            success, message = add_task(tasks, title, description, due_date)
            print(message)

        elif choice == "2":
            if not tasks:
                print("No tasks available to mark as complete.")
                continue

            display_tasks(tasks)
            selected = input("Enter the number of the task to mark complete: ").strip()
            if not selected.isdigit():
                print("Please enter a valid task number.")
                continue

            task_index = int(selected) - 1
            success, message = mark_task_as_complete(tasks, task_index)
            print(message)

        elif choice == "3":
            pending_tasks = view_pending_tasks(tasks)
            if not pending_tasks:
                print("No pending tasks.")
            else:
                display_tasks(pending_tasks)

        elif choice == "4":
            display_tasks(tasks)

        elif choice == "5":
            progress = calculate_progress(tasks)
            print(f"Progress: {progress}% complete")

        elif choice == "6":
            print("Exiting Task Management System.")
            break

        else:
            print("Invalid selection. Please choose a number from 1 to 6.")


if __name__ == "__main__":
    main()
