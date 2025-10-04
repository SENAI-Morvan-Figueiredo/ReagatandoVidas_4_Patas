from django.urls import path
from .views import dashboard_admin_adocoes

urlpatterns = [
    # Função para conseguir acessar a tela de DashBoard do Admin - Com os gatos para adoção
    path("dashboard_admin_adocoes", dashboard_admin_adocoes),
]
