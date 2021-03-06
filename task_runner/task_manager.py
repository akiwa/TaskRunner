from subprocess import Popen, PIPE
from typing import Optional, Tuple, List


class Task:
    def __init__(self, name, command):
        self._name: str = name
        self._command: str = command
        self._process: Optional[Popen] = None

    def run(self):
        self._process = Popen(self._command, shell=True, stdout=PIPE, stderr=PIPE, text=True)

    def kill(self):
        self._process.kill()

    def get_name(self):
        return self._name

    def is_running(self) -> bool:
        return self._process.poll() is None

    def get_result(self) -> Tuple[str, str]:
        return self._process.communicate()


class TaskManager:
    def __init__(self):
        self._tasks = set()

    def start_task(self, task: Task):
        self._tasks.add(task)
        task.run()

    def list_running_tasks(self) -> List[Task]:
        return [task for task in self._tasks if task.is_running()]

    def kill_all_tasks(self):
        for task in self._tasks:
            task.kill()
