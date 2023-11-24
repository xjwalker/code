class User:  # (extends_some_orm_model)

    def __init__(
            self,
            first_name: str = None,
            last_name: str = None,
            email: str = None,
            password: str = None,
            date_of_birth: str = None
    ) -> None:
        """
        Class initializer
        :param first_name: string value for first name.
        :param last_name: string value for last name.
        :param email: string value for email.
        :param password: string value for password.
        :param date_of_birth: string value for date of birth.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password  # insert some hashing
        self.date_of_birth = date_of_birth

    def to_dict(self) -> dict:
        """
        Dictionary format for client response.
        """
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "password": self.password,
            "date_of_birth": self.date_of_birth
        }
