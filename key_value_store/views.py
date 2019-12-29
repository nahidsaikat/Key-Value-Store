from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from .serializers import KeyValueSerializer
from .models import KeyValue


class KeyValueListCreateAPIView(ListCreateAPIView):
    queryset = KeyValue.objects.all().order_by('-id')
    serializer_class = KeyValueSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        contest = super().get_serializer_context()
        contest['request'] = self.request
        return contest


class KeyValueRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = KeyValue.objects.all()
    serializer_class = KeyValueSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        contest = super().get_serializer_context()
        contest['request'] = self.request
        return contest

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)
