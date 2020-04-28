from django.contrib import admin

from subscriptions.models import Subscription


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'is_active', 'activation_token', 'deletion_token',)
    search_fields = ('name', 'email',)
    list_filter = ('name', 'email', 'is_active')


admin.site.register(Subscription, SubscriptionAdmin)
