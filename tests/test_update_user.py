from helpers.url import base_url, BaseUrl


def test_update():
    response = base_url().put(BaseUrl.users_url + '/1', data={"name": "George Michael", "job": "Software Engineer"})
    response.json()
    assert response.status_code == 200
    assert str(response.json()['name']) == 'George Michael'