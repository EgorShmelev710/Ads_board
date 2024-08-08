import pytest


@pytest.mark.django_db
def test_create_user(client):
    payload = dict(
        first_name='Harry',
        last_name='Potter',
        email='harry@hogwarts.com',
        password='12345',
    )

    response = client.post('/users/', payload)

    data = response.data

    assert response.status_code == 201
    assert data['first_name'] == 'Harry'
    assert data['last_name'] == payload['last_name']
    assert data['email'] == payload['email']
    assert data['password'] != payload['password']


@pytest.mark.django_db
def test_user_token(client, user):
    response = client.post('/users/token/', dict(email='harry@hogwarts.com', password='12345'))

    assert response.status_code == 200


@pytest.mark.django_db
def test_get_user(user, auth_client):
    response = auth_client.get(f'/users/{user.pk}/')

    assert response.status_code == 200

    data = response.data

    assert data['id'] == user.id
    assert data['email'] == user.email


@pytest.mark.django_db
def test_get_all_users(auth_client):
    response = auth_client.get('/users/')

    assert response.status_code == 200


@pytest.mark.django_db
def test_update_user(user, auth_client):
    payload = dict(email='harrypotter@hogwarts.com')
    response = auth_client.patch(f'/users/{user.pk}/', payload)

    assert response.status_code == 200

    data = response.data

    assert data['email'] == 'harrypotter@hogwarts.com'


@pytest.mark.django_db
def test_delete_user(user, client):
    response_token = client.post('/users/token/', dict(email='harry@hogwarts.com', password='12345'))
    token = response_token.data.get('access')

    client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

    response = client.delete(f'/users/{user.pk}/')
    print(response.content)

    assert response.status_code == 403
