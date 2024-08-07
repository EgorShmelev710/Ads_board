import pytest
from rest_framework.test import APIClient

from ads.models import Ad, Comment
from users.models import User


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def user():
    user = User.objects.create(
        email='harry@hogwarts.com',
        first_name='Harry',
        last_name='Potter',
        is_active=True
    )
    user.set_password('12345')
    user.save()
    return user


@pytest.fixture
def second_user():
    user = User.objects.create(
        email='ron@weasly.com',
        first_name='Ron',
        last_name='Weasly',
        is_active=True
    )
    user.set_password('12345')
    user.save()
    return user


@pytest.fixture
def auth_client(client, user):
    client.force_authenticate(user=user)
    return client


@pytest.fixture
def ad(user):
    ad = Ad.objects.create(
        title='Snowboard',
        price=17000,
        author=user,
        description='Very good snowboard'
    )
    return ad


@pytest.fixture
def comment(ad, user):
    comment = Comment.objects.create(text='Really nice snowboard!', ad=ad, author=user)
    return comment
