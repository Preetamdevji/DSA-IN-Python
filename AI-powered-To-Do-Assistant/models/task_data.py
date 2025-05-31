# models/task_data.py

from dataclasses import dataclass
from datetime import datetime

@dataclass
class TaskData:
    title: str
    description: str
    created_at: datetime
    due_date: datetime
    priority: str       # e.g., "High", "Medium", "Low"
    status: bool        # False = incomplete, True = completed
    category: str       # e.g., "Work", "Personal", etc.
