from django.urls import path
from . import views

urlpatterns = [
    path("shipments", views.shipmentList),
    path("shipment/<int:pk>", views.shipmentDetails),
]
