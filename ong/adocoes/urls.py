# adocoes/urls.py
from django.urls import path
from . import views

app_name = 'adocoes'

urlpatterns = [
    path('', views.GatoListView.as_view(), name='lista'),
    path('gato/<int:pk>/', views.GatoDetailView.as_view(), name='detail'),
    path('solicitar/', views.AdocaoCreateView.as_view(), name='solicitar'),
    path('obrigado/', views.AdocaoSuccessView.as_view(), name='adocao_success'),
]