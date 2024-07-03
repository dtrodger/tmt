"""
Inventory app filters
"""

import django_filters

from interview.inventory.models import Inventory


class InventoryFilter(django_filters.FilterSet):
    created_after = django_filters.DateFilter(field_name="created_at", lookup_expr="gt")

    class Meta:
        model = Inventory
        fields = ["created_after"]
