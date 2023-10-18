def show_menu():
    print("Menu:")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as completed")
    print("4. Quit")

def add_task(todo_list):
    task = input("Enter the task: ")
    todo_list.append({"task": task, "completed": False})
    print(f"Task '{task}' added!")

def view_tasks(todo_list):
    print("\nTo-Do List:")
    for i, task in enumerate(todo_list):
        status = "✔" if task["completed"] else " "
        print(f"{i+1}. [{status}] {task['task']}")

def mark_completed(todo_list):
    view_tasks(todo_list)
    task_num = int(input("Enter the number of the task you completed: "))
    if 1 <= task_num <= len(todo_list):
        todo_list[task_num - 1]["completed"] = True
        print(f"Task {task_num} marked as completed!")
    else:
        print("Invalid task number")

def main():
    todo_list = []

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(todo_list)
        elif choice == "2":
            view_tasks(todo_list)
        elif choice == "3":
            mark_completed(todo_list)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
