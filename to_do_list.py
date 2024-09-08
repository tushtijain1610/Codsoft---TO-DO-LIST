# to_do_list.py

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({'task': task, 'completed': False})
        print(f"Added task: {task}")

    def view_tasks(self):
        if not self.tasks:
            print("Your to-do list is empty!")
        else:
            for idx, task in enumerate(self.tasks, 1):
                status = "Completed" if task['completed'] else "Not Completed"
                print(f"{idx}. {task['task']} - {status}")

    def update_task(self, task_number, completed=None, new_name=None):
        if 0 < task_number <= len(self.tasks):
            if completed is not None:
                self.tasks[task_number - 1]['completed'] = completed
                print(f"Task {task_number} marked as {'completed' if completed else 'not completed'}.")

            if new_name:
                old_name = self.tasks[task_number - 1]['task']
                self.tasks[task_number - 1]['task'] = new_name
                print(f"Task {task_number} renamed from {old_name} to {new_name}.")
        else:
            print("Invalid task number!")

    def delete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f"Deleted task: {removed_task['task']}")
        else:
            print("Invalid task number!")

    def save_tasks(self, filename="tasks.txt"):
        with open(filename, 'w') as f:
            for task in self.tasks:
                f.write(f"{task['task']},{task['completed']}\n")
        print(f"Tasks saved to {filename}")

    def load_tasks(self, filename="tasks.txt"):
        try:
            with open(filename, 'r') as f:
                self.tasks = []
                for line in f:
                    task, completed = line.strip().split(',')
                    self.tasks.append({'task': task, 'completed': completed == 'True'})
            print(f"Tasks loaded from {filename}")
        except FileNotFoundError:
            print(f"No saved tasks found in {filename}")


def menu():
    print("\nTo-Do List Menu")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Save Tasks")
    print("6. Load Tasks")
    print("7. Quit")


def main():
    to_do_list = ToDoList()
    
    while True:
        menu()
        choice = input("Enter your choice (1-7): ").strip()

        if choice == '1':
            task = input("Enter the new task: ")
            to_do_list.add_task(task)

        elif choice == '2':
            to_do_list.view_tasks()

        elif choice == '3':
            to_do_list.view_tasks()
            task_number = int(input("Enter the task number to update: "))
            action = input("Do you want to mark it as completed (c) or rename it (r)? ").strip().lower()

            if action == 'c':
                completed = input("Is the task completed? (yes/no): ").strip().lower() == 'yes'
                to_do_list.update_task(task_number, completed=completed)

            elif action == 'r':
                new_name = input("Enter the new name for the task: ")
                to_do_list.update_task(task_number, new_name=new_name)

        elif choice == '4':
            to_do_list.view_tasks()
            task_number = int(input("Enter the task number to delete: "))
            to_do_list.delete_task(task_number)

        elif choice == '5':
            filename = input("Enter filename to save (default: tasks.txt): ") or "tasks.txt"
            to_do_list.save_tasks(filename)

        elif choice == '6':
            filename = input("Enter filename to load (default: tasks.txt): ") or "tasks.txt"
            to_do_list.load_tasks(filename)

        elif choice == '7':
            print("Exiting the application.")
            break

        else:
            print("Invalid choice! Please select a valid option.")


if __name__ == "__main__":
    main()
