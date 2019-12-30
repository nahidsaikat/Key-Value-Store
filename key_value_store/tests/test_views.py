import factory
from faker import Faker

from django.urls import reverse
from django.contrib.auth import get_user_model

from .factory import KeyValueFactory

User = get_user_model()
fake = Faker()


class TestKeyValueListCreateAPIView:

    url = reverse('key_value:list-create')

    def test_create(self, auth_client):
        data = {
            fake.name(): fake.name(),
            fake.name(): fake.name(),
        }

        response = auth_client.post(self.url, data)
        assert response.status_code == 201

    def test_create_unauthorize(self, client, user):
        data = factory.build(dict, FACTORY_CLASS=KeyValueFactory, created_by=user.pk)

        response = client.post(self.url, data)

        assert response.status_code == 403

    def test_update(self, auth_client, user):
        k1 = fake.name()
        v1 = fake.name()
        k2 = fake.name()
        v2 = fake.name()
        KeyValueFactory(created_by=user, key=k1)
        KeyValueFactory(created_by=user, key=k2)
        data = {
            k1: v1,
            k2: v2
        }

        response = auth_client.patch(self.url, data)
        assert response.status_code == 200

    def test_get_list(self, auth_client, user):
        KeyValueFactory(created_by=user)
        KeyValueFactory(created_by=user)
        KeyValueFactory(created_by=user)

        response = auth_client.get(self.url)

        assert response.status_code == 200
        assert response.data.get('count') == 3

    def test_get_list_unauthorize(self, client, user):
        KeyValueFactory(created_by=user)

        response = client.get(self.url)

        assert response.status_code == 403

    def test_get_list_by_key(self, auth_client, user):
        kv1 = KeyValueFactory(created_by=user, key=fake.name())
        kv2 = KeyValueFactory(created_by=user, key=fake.name())
        KeyValueFactory(created_by=user)

        response = auth_client.get(self.url + f'?keys={kv1.key},{kv2.key}')

        assert response.status_code == 200
        assert response.data.get('count') == 2
