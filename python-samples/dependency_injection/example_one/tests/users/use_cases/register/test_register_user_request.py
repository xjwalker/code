import json

from users.use_cases.register.register_user_request import RegisterUserRequest


def test_register_user_request():
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
    register_user_request = RegisterUserRequest(event=event)
    assert register_user_request.first_name == first_name
    assert register_user_request.last_name == last_name
    assert register_user_request.password == f"{password}hashed"
    assert register_user_request.email == email
    assert register_user_request.date_of_birth == date_of_birth
