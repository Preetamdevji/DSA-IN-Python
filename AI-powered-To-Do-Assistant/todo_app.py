from custom_decorators_function.task_data import TaskData

class Task:
    def __init__(self, data: TaskData):
        self.title = data.title
        self.description = data.description
        self.created_at = data.created_at
        self.due_date = data.due_date
        self.priority = data.priority
        self.status = data.status
        self.category = data.category