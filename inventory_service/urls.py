from django.urls import path
from . import views

urlpatterns = [
    path('items', views.itemList),
    path('item/<int:pk>', views.itemDetails)
]