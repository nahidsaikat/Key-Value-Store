from django.urls import path, include
from .views import KeyValueListCreateAPIView, KeyValueRetrieveUpdateDestroyAPIView


urlpatterns = [
    path('', KeyValueListCreateAPIView.as_view(), name='list-create'),
    path('<int:pk>/', KeyValueRetrieveUpdateDestroyAPIView.as_view(), name='detail-update'),
]
