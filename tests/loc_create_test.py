import pytest


@pytest.mark.django_db
def test_loc_create(client, location):
    """
    Тестирует создание локации
    """
    send_data = {
        "name": location.name,
        "lat": location.lat,
        "lng": location.lng
    }
    expected_data = {
        "name": location.name,
        "lat": location.lat,
        "lng": location.lng
    }
    response = client.post("/location/", send_data, content_type="application/json")

    assert response.status_code == 201
    assert response.data == expected_data
