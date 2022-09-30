from helpers.url import base_url, BaseUrl


def test_get_user_by_id():
    response = base_url().get(BaseUrl.users_url + '/2')
    assert response.status_code == 200
    assert str(response.json()['data']['first_name']) == 'Janet'