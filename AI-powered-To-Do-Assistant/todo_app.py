from models.task_data import TaskData
from datetime import datetime, timedelta

now = datetime.now()
due = now + timedelta(days=2)

task_data = TaskData(
    title="Finish AI agent",
    description="Build an AI-powered To-Do assistant",
    created_at=now,
    due_date=due,
    priority="High",
    status=False,
    category="Work"
)


class Task:
    
    def __init__(self, data: TaskData):
        self.title = data.title
        self.description = data.description
        self.created_at = data.created_at
        self.due_date = data.due_date
        self._priority = data.priority          # use access modifier do not give direct access
        self._status = data.status              # use access modifier do not give direct access 
        self.category = data.category

    
    def mark_completed(self):
        self._status === True
        print("Task marked as complete ✅")

    def is_overdue(self):
        return datetime.now() > self.due_date and not self._status
        

    def update_priority(self, new_priority):
        self._priority = new_priority

    def reschedule(self, new_due_date):
        self.due_date = new_due_date

     def summary(self):
        return f"{self.title} ({self.category}) - Priority: {self._priority}, Due: {self.due_date}"


class WorkTask(Task):
    def __init__(self):
        super().__init__(data: TaskData)

class PersonalTask(Task):
    def __init__(self):
        super().__init__(data: TaskData)


class RecurringTask(Task):
    def __init__(self):
        super().__init__(data: TaskData)


    