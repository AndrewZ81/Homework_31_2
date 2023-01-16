import pytest

from advertisements.serializers import AdvertisementListViewSerializer
from tests.factories import AdFactory


@pytest.mark.django_db
def test_ad_list(client):
    """
    Тестирует выдачу списка объявлений
    """
    advertisements = AdFactory.create_batch(3)
    response = client.get("/ad/")

    assert response.status_code == 200
    assert response.data == {
        "count": 3,
        "next": None,
        "previous": None,
        "results": AdvertisementListViewSerializer(advertisements, many=True).data
    }
