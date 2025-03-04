class TaskView:
    def display_tasks(self,tasks):
        print('\n Ulohy:')
        for task in tasks:
            status = 'Dokoncena' if task.isCompleted else 'Nedokoncena'
            print(f"-{task.name}--{status}")