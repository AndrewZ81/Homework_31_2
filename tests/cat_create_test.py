import pytest

from advertisements.serializers import CategoryViewSetSerializer
from tests.factories import UserFactory


@pytest.mark.django_db
def test_cat_create(client):
    """
    Тестирует создание категории
    """
    send_data = {
        "name": "Марки",
        "slug": "stamps"

    }
    expected_data = {
        "id": 1,
        "name": "Марки",
        "slug": "stamps"
    }
    response = client.post("/cat/", send_data, content_type="application/json")

    assert response.status_code == 201
    assert response.data == expected_data
