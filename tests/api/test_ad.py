import pytest


@pytest.mark.django_db
def test_create_ad(auth_client, user):
    payload = dict(
        title='Snowboard',
        price=17000,
        author=user,
        description='Very good snowboard'
    )

    response = auth_client.post('/ads/', payload)

    assert response.status_code == 201

    data = response.data

    assert data['title'] == 'Snowboard'
    assert data['price'] == payload['price']
    assert data['author'] == user.pk
    assert data['description'] == payload['description']


@pytest.mark.django_db
def test_get_ad(user, auth_client, ad):
    response = auth_client.get(f'/ads/{ad.pk}/')

    assert response.status_code == 200

    data = response.data

    assert data['id'] == ad.id
    assert data['title'] == ad.title


@pytest.mark.django_db
def test_get_all_ads(auth_client, client):
    auth_response = auth_client.get('/ads/')
    response = client.get('/ads/')

    assert auth_response.status_code == 200
    assert response.status_code == 200


@pytest.mark.django_db
def test_update_ad(ad, auth_client):
    payload = dict(description='Very very good snowboard')
    owner_response = auth_client.patch(f'/ads/{ad.pk}/', payload)

    assert owner_response.status_code == 200

    data = owner_response.data

    assert data['description'] == 'Very very good snowboard'


@pytest.mark.django_db
def test_delete_ad(user, client, ad):
    response_token = client.post('/users/token/', dict(email='harry@hogwarts.com', password='12345'))
    token = response_token.data.get('access')

    client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

    response = client.delete(f'/ads/{ad.pk}/')

    assert response.status_code == 204


@pytest.mark.django_db
def test_create_comment(auth_client, user, ad):
    payload = dict(
        text='Really nice snowboard!',
    )

    response = auth_client.post(f'/ads/{ad.pk}/comments/create/', payload)

    assert response.status_code == 201

    data = response.data
    assert data['author'] == user.pk


@pytest.mark.django_db
def test_get_all_comments(auth_client, ad):
    response = auth_client.get(f'/ads/{ad.pk}/comments/')

    assert response.status_code == 200


@pytest.mark.django_db
def test_update_comment(auth_client, ad, comment):
    payload = dict(text='Классный скейт!')
    response = auth_client.patch(f'/ads/{ad.pk}/comments/update/{comment.id}/', payload)

    assert response.status_code == 200


@pytest.mark.django_db
def test_delete_comment(auth_client, ad, comment):
    response = auth_client.delete(f'/ads/{ad.pk}/comments/delete/{comment.id}/')

    assert response.status_code == 204
