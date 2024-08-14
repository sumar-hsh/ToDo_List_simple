# List to store tasks
tasks = []

# Function to add a task
def add_task(task):
    tasks.append({"task": task, "completed": False})
    print(f"Task '{task}' added.")

# Function to view all tasks
def view_tasks():
    if not tasks:
        print("No tasks in the list.")
        return
    for i, task in enumerate(tasks, 1):
        status = "✓" if task["completed"]== True else "✗"
        print(f"{i}. {task['task']} [{status}]")

# Function to remove a task
def remove_task(task_number):
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        print(f"Task '{removed_task['task']}' removed.")
    else:
        print("Invalid task number.")

# Function to mark a task as complete
def mark_task_complete(task_number):
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]["completed"] = True
        print(f"Task '{tasks[task_number - 1]['task']}' marked as complete.")
    else:
        print("Invalid task number.")

# Main loop
while True:
    print("\nOptions: 1) Add Task 2) View Tasks 3) Remove Task 4) Mark Task Complete 5) Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter the task: ")
        add_task(task)
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        task_num = int(input("Enter the task number to remove: "))
        remove_task(task_num)
    elif choice == "4":
        task_num = int(input("Enter the task number to mark as complete: "))
        mark_task_complete(task_num)
    elif choice == "5":
        break
    else:
        print("Invalid option. Please try again.")
