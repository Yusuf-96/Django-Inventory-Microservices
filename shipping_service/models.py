from django.db import models

class Order(models.Model):
    account_id = models.IntegerField()
    product_id = models.IntegerField()
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    class Meta:
        app_label = "shipping_service"
        db_table = "order"
        managed = False

    def __str__(self):
        return self.product_id

class Shipment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    tracking_number = models.CharField(max_length=255)
    status = models.CharField(max_length=255)

    class Meta:
        app_label = "shipping_service"
        db_table = "shipment"
        managed = False

    def __str__(self):
        return self.tracking_number
