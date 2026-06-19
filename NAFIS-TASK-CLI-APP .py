import json
import os

FILENAME = "tasks.json"

def load_tasks():
    """Load tasks from the JSON file. Returns empty list if file doesn't exist."""
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    """Save the current tasks list to the JSON file."""
    with open(FILENAME, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks):
    task_name = input("Enter the task: ")
    tasks.append({"task": task_name, "done": False})
    save_tasks(tasks)
    print("Task added successfully!")

def view_tasks(tasks):
    if not tasks:
        print("No tasks yet!")
        return
    print("\n--- Your Tasks ---")
    for index, t in enumerate(tasks, start=1):
        status = "✅" if t["done"] else "❌"
        print(f"{index}. {t['task']} [{status}]")
    print()

def mark_done(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("Enter task number to mark as done: "))
        tasks[num - 1]["done"] = True
        save_tasks(tasks)
        print("Task marked as done!")
    except (ValueError, IndexError):
        print("Invalid task number.")

def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("Enter task number to delete: "))
        removed = tasks.pop(num - 1)
        save_tasks(tasks)
        print(f"Deleted: {removed['task']}")
    except (ValueError, IndexError):
        print("Invalid task number.")

def main():
    tasks = load_tasks()
    while True:
        print("\n===== TASK MANAGER =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye! Tasks saved.")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()

