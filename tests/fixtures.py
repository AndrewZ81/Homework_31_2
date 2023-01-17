import pytest
from advertisements.models import User


@pytest.fixture
@pytest.mark.django_db
def access_token(client, django_user_model: User):
    """
    Создаёт токен доступа
    """
    username: str = "test_user"
    password: str = "test_password"
    role = "Moderator"
    email = "test@test.ru"
    birth_date = "1980-01-01"

    django_user_model.objects.create_user(
        username=username,
        password=password,
        role=role,
        email=email,
        birth_date=birth_date
    )
    response = client.post(
        "/user/token/",
        {"username": username, "password": password},
        content_type="application/json"
    )
    return response.data["access"]

