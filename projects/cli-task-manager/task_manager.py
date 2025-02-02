import json
import argparse
import os

TASKS_FILE = "tasks.json"

# Load existing tasks from file
def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as file:
        return json.load(file)

# Save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Add a new task
def add_task(title, priority):
    tasks = load_tasks()
    task = {"title": title, "priority": priority, "completed": False}
    tasks.append(task)
    save_tasks(tasks)
    print(f"✅ Task '{title}' added successfully!")

# List all tasks
def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("📌 No tasks found.")
    else:
        for idx, task in enumerate(tasks, start=1):
            status = "✅" if task["completed"] else "❌"
            print(f"{idx}. {task['title']} [Priority: {task['priority']}] - {status}")

# Mark task as completed
def complete_task(task_index):
    tasks = load_tasks()
    if 1 <= task_index <= len(tasks):
        tasks[task_index - 1]["completed"] = True
        save_tasks(tasks)
        print(f"✔️ Task {task_index} marked as completed!")
    else:
        print("⚠️ Invalid task number.")

# Delete a task
def delete_task(task_index):
    tasks = load_tasks()
    if 1 <= task_index <= len(tasks):
        removed_task = tasks.pop(task_index - 1)
        save_tasks(tasks)
        print(f"🗑 Task '{removed_task['title']}' deleted!")
    else:
        print("⚠️ Invalid task number.")

# Setup CLI arguments
def main():
    parser = argparse.ArgumentParser(description="CLI Task Manager")
    parser.add_argument("action", choices=["add", "list", "complete", "delete"], help="Action to perform")
    parser.add_argument("--title", type=str, help="Task title (required for adding)")
    parser.add_argument("--priority", type=str, choices=["low", "medium", "high"], help="Task priority")
    parser.add_argument("--task", type=int, help="Task number (for completing/deleting)")
    
    args = parser.parse_args()

    if args.action == "add":
        if not args.title or not args.priority:
            print("⚠️ Please provide --title and --priority!")
        else:
            add_task(args.title, args.priority)

    elif args.action == "list":
        list_tasks()

    elif args.action == "complete":
        if args.task is None:
            print("⚠️ Please provide --task to mark as complete.")
        else:
            complete_task(args.task)

    elif args.action == "delete":
        if args.task is None:
            print("⚠️ Please provide --task to delete.")
        else:
            delete_task(args.task)

if __name__ == "__main__":
    main()

