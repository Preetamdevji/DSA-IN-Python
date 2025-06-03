from typing import List
from task_data.task import Task


class TaskManager:
    def __init__(self):
        self.task_list : List[Task] = []

    def add_task(self, task: Task):
        self.task_list.append(task)
        print(f"✅ Task '{task.title}' added successfully.")

    
    def remove_task(self, task_id: int)
        for task in self.task_list:
            if task.task_id == task_id:
                self.task_list.remove(task)
                print(f"✅ Task '{task.title}' removed successfully.")
                return
            print("❌ Task not found.")


    def show_all_tasks(self):
        if not self.task_list:
            print("🚫 No tasks available.")
        for task in self.task_list:
            print(task.summary())


    def get_overdue_task(self):
        print("📌 Overdue Tasks:")
        for task in self.task_list:
            if task.is_overdue():
                print(task.summary())
        


    