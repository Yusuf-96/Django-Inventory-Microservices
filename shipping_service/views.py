from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import ShipmentSerializer
from .models import Shipment


@api_view(['GET'])
def shipmentList(request):
    if request.method == 'GET':
        shipments = Shipment.objects.all()
        serialzier = ShipmentSerializer(shipments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
@api_view(['GET'])   
def shipmentDetails(request, pk):
    if request.method == 'GET':
        shipment = Shipment.objects.get(pk=pk)
        serializer = ShipmentSerializer(shipment)
        return Response(serializer.data, status=status.HTTP_200_OK)
