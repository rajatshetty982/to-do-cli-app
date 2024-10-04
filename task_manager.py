class TaskManager:
    def __init__(self, data_handler):
        self.data_handler = data_handler

    def add_task(self, task_name):
        tasks = self.data_handler.load_tasks()
        new_id = max([task['id'] for task in tasks], default=0) + 1
        new_task = {
            'id': new_id,
            'name': task_name,
            'completed': False
        }
        tasks.append(new_task)
        self.data_handler.save_tasks(tasks)
        print(f"Task '{task_name}' added successfully!")

    def view_tasks(self):
        tasks = self.data_handler.load_tasks()
        if not tasks:
            print("No tasks found.")
            return
        
        print("\nYour Tasks:")
        for task in tasks:
            status = "✓" if task['completed'] else " "
            print(f"{task['id']}. [{status}] {task['name']}")

    def mark_completed(self, task_id):
        tasks = self.data_handler.load_tasks()
        for task in tasks:
            if task['id'] == task_id:
                task['completed'] = True
                self.data_handler.save_tasks(tasks)
                print(f"Task {task_id} marked as completed!")
                return
        print(f"Task with ID {task_id} not found.")

    def delete_task(self, task_id):
        tasks = self.data_handler.load_tasks()
        initial_length = len(tasks)
        tasks = [task for task in tasks if task['id'] != task_id]
        
        if len(tasks) < initial_length:
            self.data_handler.save_tasks(tasks)
            print(f"Task {task_id} deleted successfully!")
        else:
            print(f"Task with ID {task_id} not found.")