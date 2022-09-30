from helpers.url import requestSession, BaseSession


def test_update():
    response = requestSession().put(BaseSession.users_url + '/1', data={"name": "George Michael", "job": "Software Engineer"})
    response.json()
    assert response.status_code == 200
    assert str(response.json()['name']) == 'George Michael'