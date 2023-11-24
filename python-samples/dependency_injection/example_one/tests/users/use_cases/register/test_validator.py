from unittest.mock import patch

from users.use_cases.register.validator import Validator


@patch('re.match')
def test_validator(match):
    match.return_value = ["kevin"]
    body = {
        "first_name": "kevin"
    }
    validator = Validator(body=body)

    valid_body = validator.valid_body
    assert body['first_name'] == valid_body['first_name']
    assert validator.errors is None
