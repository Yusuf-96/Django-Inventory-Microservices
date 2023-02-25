from django.db import models

class Account(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    
    class Meta:
        db_table = 'account'
        
    def __str__(self):
        return self.name
    
