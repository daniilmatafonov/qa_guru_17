from helpers.url import base_url, BaseUrl


def test_users_list():
    response = base_url().get(BaseUrl.users_url, params="page=2")
    response.json()
    assert response.status_code == 200