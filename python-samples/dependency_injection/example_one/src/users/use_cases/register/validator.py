import re


class Validator:

    def __init__(self, body: dict) -> None:
        self._body = body
        self._errors = {}
        self._validated_body = {}
        self._regex_expressions = {"key": "some rules here, it could also be injected as a dependency"}

    @property
    def valid_body(self) -> dict:
        if len(self._validated_body) == 0:
            self.validate()
        return self._validated_body

    @property
    def errors(self) -> dict:
        self.validate()
        return self._errors

    def validate(self) -> None:
        for key, value in self._body.items():
            self.validate_field(key, value, self._regex_expressions[key])

    def validate_field(self, key: str, value: str, regex_exp: str) -> None:
        try:
            self._validated_body[key] = re.match(value, regex_exp)
        except ValueError as e:
            self._errors[key] = e.__traceback__
