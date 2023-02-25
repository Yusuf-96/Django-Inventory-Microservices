from django.db import models

class Shipment(models.Model):
    tracking_number = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    
    
    class Meta:
        db_table = 'shipment'
        
    def __str__(self):
        return self.tracking_number
