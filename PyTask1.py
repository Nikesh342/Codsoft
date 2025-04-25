# Simple To-Do List Application in Python (Command Line)
tasks = []

def show_tasks():
    """Display the list of tasks."""
    if not tasks:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task():
    """Add a new task."""
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f'Task "{task}" added successfully!')

def remove_task():
    """Remove a task by number."""
    show_tasks()
    try:
        task_no = int(input("Enter task number to remove: "))
        removed_task = tasks.pop(task_no - 1)
        print(f'Task "{removed_task}" removed successfully!')
    except (IndexError, ValueError):
        print("Invalid task number!")

def main():
    """Main function to run the to-do list."""
    while True:
        print("\nTo-Do List Menu:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            print("Exiting the To-Do List app. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
