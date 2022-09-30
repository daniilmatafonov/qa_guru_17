from helpers.url import requestSession, BaseSession


def test_not_found_user():
    response = requestSession().get(BaseSession.not_found_url + '/23')
    response.json()
    assert response.status_code == 404