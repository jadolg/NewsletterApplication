from django.urls import path

from subscriptions import views

urlpatterns = [
    path('', views.subscription_create, name='create-subscription'),
    path('confirm/<str:activation_token>', views.subscription_confirm, name='confirm-subscription'),
    path('delete/<str:deletion_token>', views.subscription_delete, name='delete-subscription'),
]
