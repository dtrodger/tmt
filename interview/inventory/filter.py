"""
Inventory app filters
"""
import django_filters
from interview.inventory.models import InventoryTag


class InventoryTagFilter(django_filters.FilterSet):
    order = django_filters.NumberFilter(method='filter_order')

    class Meta:
        model = InventoryTag
        fields = []

    def filter_order(self, queryset, name, value):
        return queryset.filter(inventories__orders__id=value)
