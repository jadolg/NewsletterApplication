from django.urls import path

from subscriptions import views

urlpatterns = [
    path('', views.subscription_create, name='create-subscription'),
    path('<str:pk>/confirm', views.subscription_confirm, name='confirm-subscription'),
    path('<str:pk>', views.subscription_delete, name='delete-subscription'),
]
