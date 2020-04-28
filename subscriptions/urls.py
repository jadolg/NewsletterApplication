from django.urls import path

from subscriptions import views

urlpatterns = [
    path('', views.subscription_create),
    path('confirm/<str:activation_code>', views.subscription_create),
    path('delete/<str:deletion_code>', views.subscription_delete),
]
