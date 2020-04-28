import logging

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from subscriptions.serializers import SubscriptionSerializer


@api_view(['POST', ])
def subscription_create(request):
    """
    Create an inactive subscription.
    Will send an email to the subscriber with the activation URL containing the activation token
    """
    pass


@api_view(['GET', ])
def subscription_confirm(request, activation_token):
    """
    Confirms a subscription given an activation token
    """
    pass


@api_view(['DELETE', ])
def subscription_delete(request, deletion_token):
    """
    Deletes a subscription given a deletion token
    """
    pass
