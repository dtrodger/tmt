from django.shortcuts import render
from rest_framework import generics
from django.utils.dateparse import parse_date
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from interview.order.models import Order, OrderTag
from interview.order.serializers import OrderSerializer, OrderTagSerializer


# Create your views here.
class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderTagListCreateView(generics.ListCreateAPIView):
    queryset = OrderTag.objects.all()
    serializer_class = OrderTagSerializer


class OrderViewSet(APIView):
    def get(self, request, *args, **kwargs):
        start_date_str = request.query_params.get('start_date', None)
        embargo_date_str = request.query_params.get('embargo_date', None)
        if not start_date_str or not embargo_date_str:
            return Response({'error': 'Both start_date and embargo_date parameters are required.'},
                            status=status.HTTP_400_BAD_REQUEST)

        start_date = parse_date(start_date_str)
        embargo_date = parse_date(embargo_date_str)

        if start_date is None or embargo_date is None:
            return Response({'error': 'Invalid date format.'}, status=status.HTTP_400_BAD_REQUEST)

        orders = Order.objects.filter(start_date__gte=start_date, embargo_date__lte=embargo_date)
        serializer = OrderSerializer(orders, many=True)

        return Response(serializer.data)