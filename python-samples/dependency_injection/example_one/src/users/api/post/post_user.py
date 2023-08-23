import json

from ...use_cases.register.register_user import RegisterUser
from ...use_cases.register.validator import Validator
from ...use_cases.register.register_user_request import RegisterUserRequest
from ....db.repositories.users_repository import UserRepository


def lambda_handler(event: dict, context: dict):
    user = RegisterUser(
        validator=Validator(body=event["body"]),
        register_user_request=RegisterUserRequest(event=event),
        user_repository=UserRepository()
    ).handle()

    return {
        "statusCode": 200,
        "body": json.dumps(user)
    }
