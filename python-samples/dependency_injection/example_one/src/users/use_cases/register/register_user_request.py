import json


class RegisterUserRequest:

    def __init__(self, event):
        self._body = json.loads(event["body"])

    @property
    def first_name(self):
        return self._body["first_name"]

    @property
    def last_name(self):
        return self._body["last_name"]

    @property
    def password(self):
        password = self._body.get("password")
        return f"{password}hashed"  # some hashing?

    @property
    def email(self):
        return self._body["email"]

    @property
    def date_of_birth(self):
        return self._body["date_of_birth"]
