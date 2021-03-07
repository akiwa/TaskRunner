from task_runner.task_manager import TaskManager, Task
from json import dumps


class RequestHandler:
    def __init__(self, task_manager: TaskManager):
        self._task_manager = task_manager

    def list_tasks(self) -> str:
        return dumps([f"Task: {task.get_name()} - {'still running' if is_running else 'finished'}" for (task, is_running) in self._task_manager.list_tasks()])

    def start_task(self, name: str, command: str) -> str:
        self._task_manager.start_task(Task(name, command))
        return "Task started successfully"

    def register_task(self) -> str:
        return "Route to register externally started processes"

    def finish_task(self) -> str:
        return "Updates task state to finished"

    def delete_task(self) -> str:
        return "Delete finished task after examination"
