from django.urls import path
from .views import dashboard_admin_adocoes # Você importou o nome específico

urlpatterns = [
    # Apenas use o nome que você importou
    path("dashboard_admin_adocoes", dashboard_admin_adocoes),
]
