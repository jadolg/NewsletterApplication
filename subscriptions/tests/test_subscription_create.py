from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from subscriptions.models import Subscription

UUID4_REGEX = r"[0-9a-f]{8}-?[0-9a-f]{4}-?4[0-9a-f]{3}-?[89ab][0-9a-f]{3}-?[0-9a-f]{12}"


class SubscriptionCreateTests(APITestCase):
    def test_create_subscription_with_correct_data_does_not_fail(self):
        response = self.client.post(reverse('create-subscription'), {'name': 'name1', 'email': 'email@domain.com'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, 'status code does not match')
        self.assertEqual(Subscription.objects.count(), 1, 'expected amount of objects mismatch')
        subscription = Subscription.objects.first()
        self.assertEqual(subscription.name, 'name1', 'name does not match expected value')
        self.assertEqual(subscription.email, 'email@domain.com', 'email does not match expected value')
        self.assertFalse(subscription.is_active, 'is_active is not false')
        self.assertRegex(str(subscription.activation_token), UUID4_REGEX, 'activation_token is not uuid4')
        self.assertRegex(str(subscription.deletion_token), UUID4_REGEX, 'deletion_token is not uuid4')

    def test_create_subscription_without_data_fails_and_does_not_create_objects(self):
        response = self.client.post(reverse('create-subscription'), {})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, 'status code does not match')
        self.assertEqual(Subscription.objects.count(), 0, 'expected amount of objects mismatch')

    def test_create_subscription_with_malformed_email_fails_and_does_not_create_objects(self):
        response = self.client.post(reverse('create-subscription'), {'name':'name1', 'email':'not_an_email'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, 'status code does not match')
        self.assertEqual(Subscription.objects.count(), 0, 'expected amount of objects mismatch')
