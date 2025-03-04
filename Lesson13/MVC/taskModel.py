class Task:
    def __init__(self,name):
        self.name = name
        self.isCompleted = False
    def complete(self):
        self.isCompleted = True

class TaskModel:
    def __init__(self):
        self.tasks = []
   
    def add_task(self,task):
        self.tasks.append(task)
   
    def complete_task(self):
        self.tasks.complete()
   
    def get_tasks(self):
        return self.tasks
    def count(self):
        return len(self.tasks)