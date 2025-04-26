# from typing import List

# class Task:
#     def __init__(self, description: str, due_date: str, priority: str):
#         self.description = description
#         self.due_date = due_date
#         self.priority = priority
#         self.completed = False

#     def mark_complete(self):
#         self.completed = True

#     def __str__(self):
#         status = "✔" if self.completed else "In Progress"
#         return f"[{status}] {self.description} (Due: {self.due_date}, Priority: {self.priority})"


# class Project:
#     def __init__(self, name: str):
#         self.name = name
#         self.tasks: List[Task] = []

#     def add_task(self, description: str, due_date: str, priority: str):
#         task = Task(description, due_date, priority)
#         self.tasks.append(task)

#     def list_tasks(self):
#         if not self.tasks:
#             print("📭 No tasks yet.")
#             return
#         print(f"\n📁 Project: {self.name}")
#         for i, task in enumerate(self.tasks):
#             print(f"{i + 1}. {task}")

#     def mark_task_done(self, index: int):
#         if 0 <= index < len(self.tasks):
#             self.tasks[index].mark_complete()
#             print("✅ Task marked as complete.")
#         else:
#             print("❌ Invalid task number.")

#     def show_progress(self) -> int:
#         if not self.tasks:
#             return 0
#         done = sum(task.completed for task in self.tasks)
#         return round((done / len(self.tasks)) * 100)

from datetime import datetime
from typing import List

class Task:
    def __init__(self, description: str, due_date: str, priority: str):
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = False

    def mark_complete(self):
        self.completed = True

    def __str__(self):
        status = "✔" if self.completed else "In Progress"
        return f"[{status}] {self.description} (Due: {self.due_date}, Priority: {self.priority})"


class Project:
    def __init__(self, name: str):
        self.name = name
        self.tasks: List[Task] = []

    def add_task(self, description: str, due_date: str, priority: str):
        task = Task(description, due_date, priority)
        self.tasks.append(task)

    def list_tasks(self):
        if not self.tasks:
            print("📭 No tasks yet.")
            return
        print(f"\n📁 Project: {self.name}")
        for i, task in enumerate(self.tasks):
            print(f"{i + 1}. {task}")

    def mark_task_done(self, index: int):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_complete()
            print("✅ Task marked as complete.")
        else:
            print("❌ Invalid task number.")

    def show_progress(self) -> int:
        if not self.tasks:
            return 0
        done = sum(task.completed for task in self.tasks)
        return round((done / len(self.tasks)) * 100)

    def filter_tasks(self, status: str = None, priority: str = None, due_today: bool = False):
        today = datetime.today().date()
        filtered = self.tasks

        if status == "complete":
            filtered = [task for task in filtered if task.completed]
        elif status == "incomplete":
            filtered = [task for task in filtered if not task.completed]

        if priority:
            filtered = [task for task in filtered if task.priority.lower() == priority.lower()]

        if due_today:
            filtered = [task for task in filtered if task.due_date == str(today)]

        if not filtered:
            print("📭 No tasks match your filter.")
        else:
            for i, task in enumerate(filtered):
                print(f"{i + 1}. {task}")

