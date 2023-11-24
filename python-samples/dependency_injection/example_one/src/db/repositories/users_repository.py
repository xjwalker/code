from ..models.user import User


class UserRepository:

    def create(
            self,
            first_name: str,
            last_name: str,
            email: str,
            password: str,
            date_of_birth: str
    ) -> User:
        return User(first_name, last_name, email, password, date_of_birth)
