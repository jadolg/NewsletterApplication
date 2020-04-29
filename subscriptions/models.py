import uuid

from django.db import models


class Subscription(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    name = models.CharField(max_length=250, null=False, blank=False)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f'name: {self.name} email: {self.email} ' \
               f'id: {self.id}'
