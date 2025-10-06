from django.urls import path
from .views import dashboard_admin_adocoes, excluir_gato_ajax, dashboard_admin_lar_temporario

app_name = 'gatos'  # 🔹 Define o namespace do app

urlpatterns = [
    path("dashboard_admin_adocoes", dashboard_admin_adocoes, name="dashboard_admin_adocoes"),   # Função para conseguir acessar a tela de DashBoard do Admin - Com os gatos para adoção
    path("excluir_gato_ajax/<int:gato_id>/", excluir_gato_ajax, name="excluir_gato_ajax"),    # Pop-up de confirmar exclusão
    path("dashboard_admin_lar_temporario", dashboard_admin_lar_temporario, name="dashboard_admin_lar_temporario"),    # Função para conseguir acessar a tela de DashBoard do Admin - Com os gatos para Lar_Temporario
]
