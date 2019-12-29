from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class KeyValue(models.Model):
    key = models.CharField(max_length=128)
    value = models.TextField()
    ttl = models.DecimalField(max_digits=10, decimal_places=6)

    created_by = models.ForeignKey(User, related_name='created_by', on_delete=models.DO_NOTHING)
    updated_by = models.ForeignKey(User, related_name='updated_by', on_delete=models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    inactive = models.BooleanField(default=False, blank=True, null=True)
    deleted = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return f"{self.key}: {self.value} # {self.ttl}"
