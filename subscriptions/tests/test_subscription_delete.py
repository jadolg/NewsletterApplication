import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from subscriptions.models import Subscription

UUID4_REGEX = r"[0-9a-f]{8}-?[0-9a-f]{4}-?4[0-9a-f]{3}-?[89ab][0-9a-f]{3}-?[0-9a-f]{12}"


class SubscriptionDeleteTests(APITestCase):
    def test_delete_subscription_with_existing_token_succeeds(self):
        subscription = Subscription.objects.create(name='name1', email='email@domain.com')
        self.assertEqual(Subscription.objects.count(), 1)
        response = self.client.delete(
            reverse('delete-subscription', kwargs={'deletion_token': subscription.deletion_token}))
        self.assertEqual(response.status_code, status.HTTP_200_OK, 'status code does not match')
        self.assertEqual(Subscription.objects.count(), 0)

    def test_delete_subscription_with_non_existing_token_returns_error(self):
        response = self.client.delete(
            reverse('delete-subscription', kwargs={'deletion_token': 'not really a token'}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND, 'status code does not match')
