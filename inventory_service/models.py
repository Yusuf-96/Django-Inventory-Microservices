from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField()

    class Meta:
        app_label = "inventory_service"
        db_table = "item"
        managed = False

    def __str__(self):
        return self.name
    
class Inventory(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    class Meta:
        app_label = "inventory_service"
        db_table = "inventory"
        managed = False

    def __str__(self):
        return self.product.name
