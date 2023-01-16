def test_ad_create(client):
    response = client.get("/")
    assert response.status_code == 200
