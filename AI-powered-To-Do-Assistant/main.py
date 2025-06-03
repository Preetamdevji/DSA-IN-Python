# main.py
from datetime import datetime, timedelta
from models.task_data import TaskData
from models.task import Task
from task_manager import TaskManager

# Create sample task data
now = datetime.now()
due = now + timedelta(days=2)

data = TaskData(
    title="Finish AI agent",
    description="Build an AI-powered To-Do assistant",
    created_at=now,
    due_date=due,
    priority="High",
    status=False,
    category="Work"
)

# Create Task and TaskManager
task = Task(data)
manager = TaskManager()
manager.add_task(task)

# View all tasks
manager.show_all_tasks()

# Mark task completed
task.mark_completed()

# Check overdue tasks
manager.get_overdue_tasks()
