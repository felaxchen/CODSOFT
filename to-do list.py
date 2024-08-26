# Initialize an empty to-do list
to_do_list = []


# function prints the menu options
def display_menu():
    print("To-Do List Menu:")
    print("1. Add task")
    print("2. View tasks")
    print("3. Update task")
    print("4. Delete task")
    print("5. Exit")

#function prompts the user to enter a task and adds it to list
def add_task():
    task = input("Enter a task: ")
    to_do_list.append(task)
    print("Task added successfully!")

#fuction displaya all the task
def view_tasks():
    if not to_do_list:
        print("No tasks available.")
    else:
        print("To-Do List:")
        for i, task in enumerate(to_do_list, 1):
            print(f"{i}. {task}")
            
#function allow the user to update a task by enter the task number and new task description
def update_task():
    if not to_do_list:
        print("No tasks available.")
    else:
        view_tasks()
        task_number = int(input("Enter the task number to update: "))
        if 1 <= task_number <= len(to_do_list):
            new_task = input("Enter the updated task: ")
            to_do_list[task_number - 1] = new_task
            print("Task updated successfully!")
        else:
            print("Invalid task number.")


#function allows the user to delete a task
def delete_task():
    if not to_do_list:
        print("No tasks available.")
    else:
        view_tasks()
        task_number = int(input("Enter the task number to delete: "))
        if 1 <= task_number <= len(to_do_list):
            del to_do_list[task_number - 1]
            print("Task deleted successfully!")
        else:
            print("Invalid task number.")

while True:
    display_menu()
    choice = input("Enter your choice: ")
    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        update_task()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("Exiting the application. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")