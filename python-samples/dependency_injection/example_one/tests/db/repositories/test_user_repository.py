from db.repositories.users_repository import UserRepository


def test_user_repository():
    ur = UserRepository()
    user = ur.create(first_name="fn", last_name="ln", password="pass", email="email", date_of_birth="00/00/1000")

    assert True
    assert user.first_name == "fn"
    assert user.last_name == "ln"
    assert user.email == "email"
    # todo; assert database record created through a get
