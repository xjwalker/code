# Standard
import json

# Third party
from pytest import MonkeyPatch

# Local
from .....src.users.api.post.post_user import lambda_handler
from .....src.users.use_cases.register.register_user import RegisterUser


def test_lambda_handler(monkeypatch: MonkeyPatch):
    mock_response = {"mock": "response"}
    monkeypatch.setattr(RegisterUser, "handle", lambda x: mock_response)
    response = lambda_handler({"body": json.dumps({})}, context={})
    assert response["body"] == json.dumps(mock_response)
    assert response["statusCode"] == 200
