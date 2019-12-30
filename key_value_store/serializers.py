from rest_framework import serializers

from .models import KeyValue


class KeyValueSerializer(serializers.ModelSerializer):

    @property
    def request(self):
        return self.context.get('request')

    def to_internal_value(self, data):
        if self.request and self.request.user:
            _mutable = data._mutable
            data._mutable = True
            data['created_by'] = self.request.user.pk
            data._mutable = _mutable
        ret = super().to_internal_value(data)
        return ret

    class Meta:
        model = KeyValue
        fields = '__all__'
