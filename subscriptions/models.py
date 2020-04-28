import uuid

from django.db import models


class Subscription(models.Model):
    name = models.CharField(max_length=250, null=False, blank=False)
    email = models.EmailField(unique=True)
    activation_token = models.UUIDField(default=uuid.uuid4, editable=False)
    deletion_token = models.UUIDField(default=uuid.uuid4, editable=False)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}  {self.email}'
