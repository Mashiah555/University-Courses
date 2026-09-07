# Yuval Mashiah
# Structure of Programming Languages
# HW Assignment 2 Question 6

def task_manager():
    """
    Creates a task manager closure that encapsulates a dictionary of tasks.
    Returns a dictionary of functions to interact with the tasks state.
    """
    # This dictionary is the enclosed state, accessible only by the inner functions
    tasks = {}

    def add_task(task: str, status: str = "incomplete"):
        """
        Adds a new task to the tasks dictionary.
        The default status is 'incomplete' if not provided.
        """
        tasks[task] = status

    def get_tasks() -> dict:
        """
        Returns the current dictionary representing all tasks and their statuses.
        """
        return tasks

    def complete_task(task: str):
        """
        Changes the status of an existing task to 'complete'.
        If the task does not exist, it does nothing.
        """
        if task in tasks:
            tasks[task] = "complete"

    # Return a dictionary that exposes the inner functions, 
    # creating the closure over the 'tasks' dictionary.
    return {
        'add_task': add_task,
        'get_tasks': get_tasks,
        'complete_task': complete_task
    }


def main():
    """
    Main script demonstrating the usage of the task manager,
    matching the example provided in the assignment.
    """
    # Create a new task manager
    tasks_manager = task_manager()
    
    # Add tasks using the exposed function in the dictionary
    tasks_manager['add_task']("Write email")
    tasks_manager['add_task']("Shopping", "in progress")
    tasks_manager['add_task']("Homework")
    
    # Get the list of tasks
    current_tasks = tasks_manager['get_tasks']()
    print("Tasks after adding:")
    print(current_tasks)

    # Mark a task as complete
    tasks_manager['complete_task']("Write email")
    
    # Get the list of tasks after marking it complete
    current_tasks = tasks_manager['get_tasks']()
    print("\nTasks after completing 'Write email':")
    print(current_tasks)

if __name__ == "__main__":
    main()