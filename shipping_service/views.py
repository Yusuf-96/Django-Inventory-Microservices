from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import OrderSerializer
from .models import Shipment, Order


@api_view(["GET", "POST"])
def orderList(request):
    if request.method == "GET":
        orders = Order.objects.using("shipping_service").all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def orderDetails(request, pk):
    try:
        order = Order.objects.using("shipping_service").get(pk=pk)
    except Order.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == "PUT":
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
