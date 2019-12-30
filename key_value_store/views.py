from rest_framework import status, mixins
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated

from .serializers import KeyValueSerializer
from .models import KeyValue


class KeyValueListCreateAPIView(ListCreateAPIView, mixins.UpdateModelMixin):
    queryset = KeyValue.objects.all().order_by('-id')
    serializer_class = KeyValueSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        contest = super().get_serializer_context()
        contest['request'] = self.request
        return contest

    def get_queryset(self):
        queryset = super().get_queryset()
        keys = self.request.GET.get('keys', None)
        if keys:
            queryset = queryset.filter(key__in=keys.split(','), ttl__gt=0)
        return queryset

    def create(self, request, *args, **kwargs):
        for key, value in request.data.items():
            data = {
                'key': key,
                'value': value,
                'ttl': 300
            }
            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        for key, value in request.data.items():
            instance = self.get_queryset().filter(key=key).first()
            data = {
                'id': instance.pk,
                'key': key,
                'value': value,
                'ttl': 300
            }

            serializer = self.get_serializer(instance=instance, data=data)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)
