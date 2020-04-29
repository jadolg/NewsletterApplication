from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from subscriptions.models import Subscription
from subscriptions.serializers import SubscriptionSerializer


@api_view(['POST', ])
def subscription_create(request):
    """
    Create an inactive subscription.
    Will send an email to the subscriber with the activation URL containing the activation token
    """
    serializer = SubscriptionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        # TODO: Send an email to the subscriber containing the activation code
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST', ])
def subscription_confirm(request, id):
    """
    Confirms a subscription given an activation token
    """
    subscription = get_object_or_404(Subscription.objects.all(), id=id)
    subscription.is_active = True
    subscription.save()
    serializer = SubscriptionSerializer(subscription)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['DELETE', ])
def subscription_delete(request, id):
    """
    Deletes a subscription given a deletion token
    """
    subscription = get_object_or_404(Subscription.objects.all(), id=id)
    serializer = SubscriptionSerializer(subscription)
    subscription.delete()
    return Response(serializer.data, status=status.HTTP_200_OK)
