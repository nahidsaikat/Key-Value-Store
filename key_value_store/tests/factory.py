from factory.django import DjangoModelFactory
from faker import Faker

from ..models import KeyValue

fake = Faker()


class KeyValueFactory(DjangoModelFactory):
    class Meta:
        model = KeyValue

    key = fake.name()
    value = fake.name()
    ttl = 5
