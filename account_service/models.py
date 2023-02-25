from django.db import models


class Account(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)

    class Meta:
        app_label = "account_service"
        db_table = "account"
        managed = False

    def __str__(self):
        return self.name


class Address(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=10)
    
    class Meta:
        app_label = "account_service"
        db_table = "address"
        managed = False

    def __str__(self):
        return self.account.name
