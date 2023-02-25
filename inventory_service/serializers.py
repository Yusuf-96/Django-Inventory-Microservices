from rest_framework import serializers
from .models import Item, Inventory


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = "__all__"


class ItemSerialier(serializers.ModelSerializer):
    inventory = InventorySerializer(many=True, read_only=True)

    class Meta:
        model = Item
        fields = "__all__"
