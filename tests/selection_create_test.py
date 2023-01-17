import pytest

from tests.factories import AdFactory


@pytest.mark.django_db
def test_selection_create(client, access_token, user):
    """
    Тестирует создание подборки объявлений
    """
    advertisements = AdFactory.create_batch(4)

    send_data = {
        "name": "Моя подборка",
        "owner": user.id,
        "items": [ad.id for ad in advertisements]
    }
    expected_data = {
        "id": 1,
        "name": "Моя подборка",
        "owner": user.id,
        "items": [ad.id for ad in advertisements]
    }
    response = client.post("/selection/create/", send_data, HTTP_AUTHORIZATION="Bearer " + access_token)

    assert response.status_code == 201
    assert response.data == expected_data
