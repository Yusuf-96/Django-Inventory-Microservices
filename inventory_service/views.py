from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import ItemSerialier
from .models import Item


@api_view(["GET"])
def itemList(request):
    if request.method == "GET":
        items = Item.objects.all()
        serializer = ItemSerialier(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def itemDetails(request, pk):
    if request.method == "GET":
        item = Item.objecs.get(pk=pk)
        serializer = ItemSerialier(item)
        return Response(serializer.data, status=status.HTTP_200_OK)
