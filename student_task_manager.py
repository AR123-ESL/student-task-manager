import json

FILE_NAME = "tasks.json"

def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file)

def add_task(tasks):
    task = input("Enter task: ")
    tasks.append(task)
    save_tasks(tasks)

def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def delete_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter task number to delete: ")) - 1
        tasks.pop(index)
        save_tasks(tasks)
    except:
        print("Invalid selection.")

def main():
    tasks = load_tasks()

    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            break
        else:
            print("Invalid option")

main()