"""
Inventory app filters
"""
import django_filters
from interview.order.models import Order


class OrderFilter(django_filters.FilterSet):
    tag = django_filters.NumberFilter(method='filter_tag')

    class Meta:
        model = Order
        fields = []

    def filter_tag(self, queryset, name, value):
        return queryset.filter(inventory__tags__id=value)
