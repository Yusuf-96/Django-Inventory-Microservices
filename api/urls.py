from django.urls import path, include

urlpatterns = [
    path("accounts/", include("account_service.urls")),
    path("inventory/", include("inventory_service.urls")),
    path("shipping/", include("shipping_service.urls")),
]
