from helpers.url import requestSession, BaseSession


def test_users_list():
    response = requestSession().get(BaseSession.users_url, params="page=2")
    response.json()
    assert response.status_code == 200