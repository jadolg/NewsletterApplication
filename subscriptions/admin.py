from django.contrib import admin
from subscriptions.models import Subscription


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'activation_token', 'deletion_token',)
    search_fields = ('name', 'email',)
    list_filter = ('name', 'email',)


admin.site.register(Subscription, SubscriptionAdmin)
