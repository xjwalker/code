from .register_user_request import RegisterUserRequest
from .validator import Validator
from db.repositories.users_repository import UserRepository


class RegisterUser:

    def __init__(
        self,
        validator: Validator,
        register_user_request: RegisterUserRequest,
        user_repository: UserRepository
    ) -> None:
        self._register_user_request = register_user_request
        self._user_repository = user_repository
        self._validator = validator

    def handle(self) -> dict:
        self._validator.validate()
        if self._validator.errors is not None:
            return {"error": "raise exception or something"}

        first_name = self._register_user_request.first_name
        user = self._user_repository.create(
            first_name=first_name,
            last_name=self._register_user_request.last_name,
            password=self._register_user_request.password,
            email=self._register_user_request.email,
            date_of_birth=self._register_user_request.date_of_birth
        )

        return user.to_dict()
