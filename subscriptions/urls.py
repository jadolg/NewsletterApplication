from django.urls import path, include

from subscriptions import views

urlpatterns = [
    path('', views.subscription_create, name='create-subscription'),
    path('<str:id>/confirm', views.subscription_confirm, name='confirm-subscription'),
    path('<str:id>', views.subscription_delete, name='delete-subscription'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
