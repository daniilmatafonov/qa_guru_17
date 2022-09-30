from helpers.url import requestSession, BaseSession


def test_get_user_by_id():
    response = requestSession().get(BaseSession.users_url + '/2')
    response.json()
    assert response.status_code == 200
    assert str(response.json()['data']['first_name']) == 'Janet'