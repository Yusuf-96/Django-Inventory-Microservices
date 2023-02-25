from rest_framework import serializers
from .models import Shipment

class ShipmentSerializer(serializers.ModelSerialier):
    class Meta:
        model = Shipment
        fields = '__all__'