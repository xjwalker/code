import re


class Validator:

    def __init__(self, body: dict) -> None:
        self._body = body
        self._errors = {}
        self._validated_body = {}
        self._regex_expressions = {
            "first_name": "^[a-zA-Z]+$"
        }

    @property
    def valid_body(self) -> dict:
        if len(self._validated_body) == 0:
            self.validate()
        return self._validated_body

    @property
    def errors(self) -> dict:
        self.validate()
        return self._errors if len(self._errors) else None

    def validate(self) -> None:
        for key, value in self._body.items():
            self.validate_field(key, value)

    def validate_field(self, key: str, value: str) -> None:
        try:
            # WIP: code
            if key in self._regex_expressions:
                regex = self._regex_expressions[key]
                res = re.match(value, regex)
                if res is not None:
                    self._validated_body[key] = res[0]
        except ValueError as e:
            self._errors[key] = e.__traceback__
