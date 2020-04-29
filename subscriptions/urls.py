from django.urls import path, include

from subscriptions import views

urlpatterns = [
    path('', views.subscription_create, name='create-subscription'),
    path('confirm/<str:activation_token>', views.subscription_confirm, name='confirm-subscription'),
    path('delete/<str:deletion_token>', views.subscription_delete, name='delete-subscription'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
