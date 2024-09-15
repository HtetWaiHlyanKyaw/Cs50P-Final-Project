from datetime import date
class Task:
    def __init__(
        self,
        id,
        task,
        priority,
        deadline,
        status=False,
        created=date.today(),
        completed=None,
    ):
        self._id = id
        self._task = task
        self._priority = priority
        self._deadline = deadline
        self._created = created
        self._status = status
        self._completed = completed

    def __str__(self):
        return f"ID: {self.id}|Task: {self.task}|priority: {self.priority}|deadline: {self.deadline}|status:  {self.status}|created at: {self.created}|completed at: {self.completed}"

    @property
    def id(self):
        return self._id

    @property
    def task(self):
        return self._task

    @property
    def priority(self):
        return self._priority

    @property
    def deadline(self):
        return self._deadline

    @property
    def status(self):
        return "completed" if self._status else "unfinished"

    @property
    def created(self):
        return self._created

    @property
    def completed(self):
        return self._completed

    @status.setter
    def status(self, status):
        self._status = status

    @completed.setter
    def completed(self, completed):
        self._completed = completed
