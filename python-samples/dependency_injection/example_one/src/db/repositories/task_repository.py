from ..models.task import Task


class TaskRepository:

    def update(
            self,
            first_name: str,
            last_name: str,
            email: str,
            password: str,
            date_of_birth: str
    ) -> Task:
        # code to update a task
        pass

    def get_tasks_to_notify(self, date, limit, offset):
        # nice query or ORM function to get tasks by date with limit and offset to paginate
        pass
