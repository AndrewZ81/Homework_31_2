import pytest

from advertisements.serializers import AdvertisementDetailViewSerializer
from tests.factories import AdFactory


@pytest.mark.django_db
def test_ad_detail(client, access_token):
    """
    Тестирует выдачу одного объявлений
    """
    advertisement = AdFactory.create()
    response = client.get(f"/ad/{advertisement.id}/", HTTP_AUTHORIZATION="Bearer " + access_token)

    assert response.status_code == 200
    assert response.data == AdvertisementDetailViewSerializer(advertisement).data
