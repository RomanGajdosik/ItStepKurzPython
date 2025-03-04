from taskModel import Task 

class TaskController:
    def __init__(self,model,view):
        self.model = model
        self.view = view

    def add_task(self,name):
        task =Task(name)
        self.model.add_task(task) # ak napisem self.model.add_task(Task(name)) tak to bude chyba lebo to ocakava objekt a nie string
    def complete_task(self,name):
        for task in self.model.get_tasks():
            if task.name == name:
                task.complete()
    def display_tasks(self):
        task =self.model.get_tasks()
        self.view.display_tasks(task)
    def get_task(self,index):
        task = self.model.get_task(index)
        return task
    def get_tasks_number(self):
       print(f"Pocet uloh je : {self.model.count()}")


