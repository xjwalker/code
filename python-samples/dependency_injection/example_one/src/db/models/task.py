class Task:

    def __init__(self):
        self.name = ""
        self.due_date = ""
        self.assigned_to = ""  # user_id FK?
        self.created_at = ""
        pass

    def to_dict(self):
        return {
            "name": self.name,
            "due_date": self.due_date,
            "assigned_to": self.assigned_to,
            "created_at": self.created_at
        }
