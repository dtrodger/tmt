"""
Order app filters
"""

import django_filters
from interview.order.models import Order


class OrderFilter(django_filters.FilterSet):
    start_date_after = django_filters.DateFilter(field_name="start_date", lookup_expr='gte')
    embargo_date_before = django_filters.DateFilter(field_name="embargo_date", lookup_expr='lte')

    class Meta:
        model = Order
        fields = ['start_date_after', 'embargo_date_before']
