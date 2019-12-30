from django.urls import path, include
from .views import KeyValueListCreateAPIView


urlpatterns = [
    path('', KeyValueListCreateAPIView.as_view(), name='list-create'),
]
