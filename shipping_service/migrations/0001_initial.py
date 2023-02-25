# Generated by Django 4.1.7 on 2023-02-25 15:14

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("account_id", models.IntegerField()),
                ("product_id", models.IntegerField()),
                ("quantity", models.IntegerField()),
                ("total_price", models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                "db_table": "order",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Shipment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("tracking_number", models.CharField(max_length=255)),
                ("status", models.CharField(max_length=255)),
            ],
            options={
                "db_table": "shipment",
                "managed": False,
            },
        ),
    ]
