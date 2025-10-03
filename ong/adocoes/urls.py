# adocoes/urls.py
from django.urls import path
from . import views

app_name = 'adocoes'

urlpatterns = [
    path('', views.GatoListView.as_view(), name='lista'),
    path('gato/<int:pk>/', views.GatoDetailView.as_view(), name='detail'),
    path('solicitar/', views.formulario_adocao, name='solicitar'),
    path('obrigado/', views.formulario_sucesso, name='adocao_success'),
]