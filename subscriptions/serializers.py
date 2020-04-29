from django.conf import settings
from rest_framework import serializers

from subscriptions.models import Subscription


class SubscriptionSerializer(serializers.ModelSerializer):
    is_active = serializers.BooleanField(read_only=True)

    if settings.DEBUG:
        id = serializers.UUIDField(read_only=True)

    class Meta:
        model = Subscription
        if settings.DEBUG:
            fields = ['name', 'email', 'is_active', 'id']
        else:
            fields = ['name', 'email', 'is_active']
