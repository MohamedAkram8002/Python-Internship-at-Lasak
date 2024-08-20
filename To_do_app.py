import json

# To store tasks
tasks = []

def add_task(task):
    tasks.append({"task": task, "completed": False})

def view_tasks():
    if not tasks:
        print("No tasks to show.")
    for idx, task in enumerate(tasks, 1):
        status = "Completed" if task['completed'] else "Not Completed"
        print(f"{idx}. {task['task']} [{status}]")

def delete_task(task_number):
    if 0 < task_number <= len(tasks):
        tasks.pop(task_number - 1)
    else:
        print("Invalid task number.")

def complete_task(task_number):
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]['completed'] = True
    else:
        print("Invalid task number.")

def save_tasks(filename='tasks.json'):
    with open(filename, 'w') as file:
        json.dump(tasks, file)

def load_tasks(filename='tasks.json'):
    try:
        with open(filename, 'r') as file:
            global tasks
            tasks = json.load(file)
    except FileNotFoundError:
        print(f"{filename} not found. Starting with an empty task list.")

def main():
    load_tasks()
    while True:
        print("\nTo-Do App:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Mark Task as Completed")
        print("5. Save and Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task: ")
            add_task(task)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            task_number = int(input("Enter the task number to delete: "))
            delete_task(task_number)
        elif choice == '4':
            task_number = int(input("Enter the task number to mark as completed: "))
            complete_task(task_number)
        elif choice == '5':
            save_tasks()
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
