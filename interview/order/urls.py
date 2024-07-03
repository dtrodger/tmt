from django.urls import path
from interview.order.views import OrderListCreateView, OrderTagListCreateView, OrderViewSet


urlpatterns = [
    path("tags/", OrderTagListCreateView.as_view(), name="order-detail"),
    path("", OrderListCreateView.as_view(), name="order-list"),
    path("orders/", OrderViewSet.as_view(), name="order-list"),
]
