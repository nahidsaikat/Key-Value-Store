import faker
import pytest
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model

User = get_user_model()
fake = faker.Faker()


@pytest.fixture(scope='session')
def django_db_modify_db_settings():
    pass


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def user(db):
    user = User.objects.create(username=fake.name(), password=fake.name())
    user.save()
    return user


@pytest.fixture
def auth_client(client, user):
    client.force_authenticate(user)
    return client


@pytest.fixture
def client2():
    return APIClient()


@pytest.fixture
def user2(db):
    user = User.objects.create(username=fake.name(), password=fake.name())
    user.save()
    return user


@pytest.fixture
def auth_client2(client2, user2):
    client.force_authenticate(user2)
    return client
