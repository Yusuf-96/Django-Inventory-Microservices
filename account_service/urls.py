from django.urls import path
from . import views

urlpatterns = [
    path("users", views.getAccountList),
    path("user/<int:pk>", views.getAccountDetails),
]
