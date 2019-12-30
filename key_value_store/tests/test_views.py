import factory
from faker import Faker
from decimal import Decimal

from django.urls import reverse
from django.contrib.auth import get_user_model

from .factory import KeyValueFactory

User = get_user_model()
fake = Faker()


class TestKeyValueListCreateAPIView:

    url = reverse('key_value:list-create')

    def test_create(self, auth_client):
        key = fake.name()
        value = fake.name()
        data = factory.build(dict, FACTORY_CLASS=KeyValueFactory, key=key, value=value)

        response = auth_client.post(self.url, data)

        assert response.status_code == 201
        assert response.data.get('key') == key
        assert response.data.get('value') == value
        assert Decimal(response.data.get('ttl')) == Decimal(5.0)

    def test_create_unauthorize(self, client, user):
        data = factory.build(dict, FACTORY_CLASS=KeyValueFactory, created_by=user.pk)

        response = client.post(self.url, data)

        assert response.status_code == 403

    def test_get_list(self, auth_client, user):
        KeyValueFactory(created_by=user)
        KeyValueFactory(created_by=user)
        KeyValueFactory(created_by=user)

        response = auth_client.get(self.url)

        assert response.status_code == 200
        assert response.data.get('count') == 3

    def test_get_list_unauthorize(self, client, user):
        KeyValueFactory(created_by=user)
        KeyValueFactory(created_by=user)
        KeyValueFactory(created_by=user)

        response = client.get(self.url)

        assert response.status_code == 403
