from django.urls import path
from .views import dashboard_admin_adocoes, excluir_gato_ajax
from . import views

app_name = 'gatos'

urlpatterns = [
    path("dashboard_admin_adocoes", dashboard_admin_adocoes),   # Função para conseguir acessar a tela de DashBoard do Admin - Com os gatos para adoção
    path("excluir_gato_ajax/<int:gato_id>/", excluir_gato_ajax, name="excluir_gato_ajax"),    # Pop-up de confirmar exclusão
    path('adicionar/', views.adicionar_gato, name='adicionar_gato'),
]
