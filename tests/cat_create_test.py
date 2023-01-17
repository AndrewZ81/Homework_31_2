import pytest


@pytest.mark.django_db
def test_cat_create(client):
    """
    Тестирует создание категории
    """
    send_data = {
        "name": "Тестовая категория",
        "slug": "test_cat"
    }
    expected_data = {
        "name": "Тестовая категория",
        "slug": "test_cat"
    }
    response = client.post("/cat/", send_data, content_type="application/json")

    assert response.status_code == 201
    assert response.data == expected_data
