from dataclasses import dataclass

@dataclass
class TaskData:
    title: str
    description: str
    created_at: int
    due_date: int
    priority: str
    status: bool
    category: str