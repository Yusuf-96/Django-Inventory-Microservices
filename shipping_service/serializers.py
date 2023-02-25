from rest_framework import serializers
from .models import Shipment, Order


class ShipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipment
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    shipments = ShipmentSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = "__all__"
