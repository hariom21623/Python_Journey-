import json
import os

FILE_NAME = "Beginner\\To-Do App\\tasks.json"

# -----------------------------
# Load tasks from file
# -----------------------------
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return []

# -----------------------------
# Save tasks to file
# -----------------------------
def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f, indent=4)

# -----------------------------
# Show all tasks
# -----------------------------
def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks available.\n")
        return

    print("\nYour Tasks:")
    for i, task in enumerate(tasks):
        status = "✅" if task["completed"] else "❌"
        print(f"{i+1}. {task['title']} [{status}]")
    print()

# -----------------------------
# Add new task
# -----------------------------
def add_task(tasks):
    title = input("Enter task: ")

    task = {
        "title": title,
        "completed": False
    }

    tasks.append(task)
    save_tasks(tasks)

    print("Task added successfully!")

# -----------------------------
# Delete task
# -----------------------------
def delete_task(tasks):
    view_tasks(tasks)
    try:
        num = int(input("Enter task number to delete: "))
        tasks.pop(num - 1)
        save_tasks(tasks)
        print("Task deleted.")
    except:
        print("Invalid input!")

# -----------------------------
# Mark task as completed
# -----------------------------
def mark_completed(tasks):
    view_tasks(tasks)
    try:
        num = int(input("Enter task number to mark completed: "))
        tasks[num - 1]["completed"] = True
        save_tasks(tasks)
        print("Task marked as completed.")
    except:
        print("Invalid input!")

# -----------------------------
# Main program loop
# -----------------------------
def main():
    tasks = load_tasks()

    while True:
        print("\n--- TO-DO APP ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Mark Task Completed")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            delete_task(tasks)

        elif choice == "4":
            mark_completed(tasks)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice!")

# Run app
if __name__ == "__main__":
    main()