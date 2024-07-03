from django.urls import path
from interview.order.views import OrderListCreateView, OrderTagListCreateView, OrderView


urlpatterns = [
    path("tags/", OrderTagListCreateView.as_view(), name="order-detail"),
    path("", OrderListCreateView.as_view(), name="order-list"),
    path("orders/", OrderView.as_view(), name="order-list")

]
