from taskControler import TaskController
from taskModel import TaskModel
from taskView import TaskView

model = TaskModel()
view = TaskView()
taskControler = TaskController(model,view)

taskControler.add_task('Umyt auto')
taskControler.add_task('Umyt okna')
taskControler.add_task('Umyt podlahu')


taskControler.complete_task("Umyt auto")
taskControler.display_tasks()
taskControler.get_tasks_number()























