from django.contrib import admin

from interview.order.models import OrderTag, Order


class OrderTagAdmin(admin.ModelAdmin):
    """
    OrderTagAdmin admin
    """


class OrderAdmin(admin.ModelAdmin):
    """
    Order admin
    """


admin.site.register(OrderTag, OrderTagAdmin)
admin.site.register(Order, OrderAdmin)
