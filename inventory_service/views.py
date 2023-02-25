from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import ItemSerialier
from .models import Item


@api_view(["GET", "POST"])
def itemList(request):
    if request.method == "GET":
        items = Item.objects.using("inventory_service").all()
        serializer = ItemSerialier(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == "POST":
        serializer = ItemSerialier(data=request.data)
        if serializer.is_valid():
            serializer.save(using="inventory_service")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def itemDetails(request, pk):
    try:
        item = Item.objecs.using("inventory_service").get(pk=pk)
    except Item.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = ItemSerialier(item)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'PUT':
        serializer = ItemSerialier(item, data=request.data)
        if serializer.is_valid():
            serializer.save(using='inventory_service')
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        item.delete(using='inventory_service')
        return Response(status=status.HTTP_204_NO_CONTENT)
