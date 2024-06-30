from django.contrib import admin
from .models import Order
# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'plan',
        'order_number',
        'full_name',
        'date',
        'order_total',
        'stripe_pid'
    )

    ordering = ('plan',)

admin.site.register(Order, OrderAdmin)
