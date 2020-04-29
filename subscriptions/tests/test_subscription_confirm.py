import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from subscriptions.models import Subscription

UUID4_REGEX = r"[0-9a-f]{8}-?[0-9a-f]{4}-?4[0-9a-f]{3}-?[89ab][0-9a-f]{3}-?[0-9a-f]{12}"


class SubscriptionConfirmTests(APITestCase):
    def test_confirm_subscription_with_existing_token_succeeds(self):
        subscription = Subscription.objects.create(name='name1', email='email@domain.com')
        response = self.client.post(
            reverse('confirm-subscription', kwargs={'pk': subscription.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK, 'status code does not match')
        subscription.refresh_from_db()
        self.assertTrue(subscription.is_active, 'subscription is not active')
        self.assertEqual(json.loads(response.content),
                         {'name': 'name1', 'email': 'email@domain.com', 'is_active': True}, 'expected result mismatch')

    def test_confirm_subscription_with_non_existing_token_returns_error(self):
        response = self.client.post(
            reverse('confirm-subscription', kwargs={'pk': 'not really an id'}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND, 'status code does not match')
