# To-Do List Application

tasks = []

def view_tasks():
    if not tasks:
        print("No tasks found!")
    else:
        for i, task in enumerate(tasks, 1):
            status = "[X]" if task['completed'] else "[ ]"
            print(f"{i}. {task['name']} {status}")

def add_task():
    task_name = input("Enter the task: ")
    tasks.append({"name": task_name, "completed": False})
    print("Task added!")

def mark_completed():
    view_tasks()
    try:
        task_num = int(input("Which task number would you like to mark as completed? "))
        tasks[task_num - 1]['completed'] = True
        print("Task marked as completed!")
    except (IndexError, ValueError):
        print("Invalid task number.")

def delete_task():
    view_tasks()
    try:
        task_num = int(input("Which task number would you like to delete? "))
        tasks.pop(task_num - 1)
        print("Task deleted!")
    except (IndexError, ValueError):
        print("Invalid task number.")

while True:
    print("\n1. View Tasks\n2. Add a Task\n3. Mark a Task as Completed\n4. Delete a Task\n5. Exit")
    choice = input("Choose an option: ")
    if choice == '1':
        view_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        mark_completed()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")
