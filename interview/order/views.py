from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from interview.order.models import Order, OrderTag
from interview.order.serializers import OrderSerializer, OrderTagSerializer
from interview.inventory.models import InventoryTag


class OrderView(APIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
    def get(self, request, *args, **kwargs):
        tag_id = request.query_params.get('tag_id', None)
        if tag_id is None:
            return Response({'error': 'tag_id parameter is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            tag_id = int(tag_id)
            orders = Order.objects.filter(inventories__tags__id=tag_id).distinct()
        except ValueError:
            return Response({'error': 'Invalid tag_id format'}, status=status.HTTP_400_BAD_REQUEST)
        except InventoryTag.DoesNotExist:
            return Response({'error': 'Tag not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(orders, many=True)
        return Response(serializer.data)

# Create your views here.
class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderTagListCreateView(generics.ListCreateAPIView):
    queryset = OrderTag.objects.all()
    serializer_class = OrderTagSerializer
