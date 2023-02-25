from django.urls import path
from . import views

urlpatterns = [
    path("shipments", views.orderList),
    path("shipment/<int:pk>", views.orderDetails),
]
