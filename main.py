
import os
import task_manager
from data_handler import DataHandler

def display_menu():
    print("\n=== To-Do List App ===")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Quit")

def main():
    data_handler = DataHandler()
    manager = task_manager.TaskManager(data_handler)
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            task_name = input("Enter task name: ")
            manager.add_task(task_name)
        elif choice == '2':
            manager.view_tasks()
        elif choice == '3':
            task_id = input("Enter task ID to mark as completed: ")
            try:
                manager.mark_completed(int(task_id))
            except ValueError:
                print("Please enter a valid task ID (number)")
        elif choice == '4':
            task_id = input("Enter task ID to delete: ")
            try:
                manager.delete_task(int(task_id))
            except ValueError:
                print("Please enter a valid task ID (number)")
        elif choice == '5':
            print("Thank you for using the To-Do List App!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()