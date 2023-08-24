# Standard
import json
from unittest.mock import Mock

# Third party
import pytest

from db.models.user import User
# Local
from users.use_cases.register.register_user import RegisterUser
from users.use_cases.register.validator import Validator
from users.use_cases.register.register_user_request import RegisterUserRequest
from db.repositories.users_repository import UserRepository


def test_register_user_without_mocks():
    first_name = "kevin"
    last_name = "walker"
    password = "password"
    email = "kevin@email.com"
    date_of_birth = "06/07/1995"

    event = {
        "body": json.dumps({
            "first_name": first_name,
            "last_name": last_name,
            "password": password,
            "email": email,
            "date_of_birth": date_of_birth,
        })
    }
    register_user = RegisterUser(
        validator=Validator(json.loads(event["body"])),
        register_user_request=RegisterUserRequest(event),
        user_repository=UserRepository(),
    )
    response = register_user.handle()
    assert response == {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "password": f"{password}hashed",
        "date_of_birth": date_of_birth
    }
    # todo; assert database record was created


def test_register_user_with_mocks():
    register_user_request = Mock()
    register_user_request.first_name.return_value = "kevin"
    register_user_request.last_name = "walker"
    register_user_request.password = "crushcrush"
    register_user_request.email = "kevin"
    register_user_request.date_of_birth = "kevin"

    user_mock = Mock()
    user_mock.to_dict.return_value = {"fake": "user"}
    user_repository = Mock()
    user_repository.create.return_value = user_mock

    validator = Mock()
    validator.errors = None
    register_user = RegisterUser(
        validator=validator,
        register_user_request=register_user_request,
        user_repository=user_repository,
    ).handle()

    validator.validate.assert_called_once()
    user_repository.create.assert_called_once()
    assert register_user == {"fake": "user"}


@pytest.mark.live
def test_live_api_call():
    pass
