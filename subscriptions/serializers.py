from rest_framework import serializers

from subscriptions.models import Subscription


class SubscriptionSerializer(serializers.ModelSerializer):
    is_active = serializers.BooleanField(read_only=True)

    class Meta:
        model = Subscription
        fields = ['name', 'email', 'is_active']
