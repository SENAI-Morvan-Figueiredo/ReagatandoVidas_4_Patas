from django.urls import path
from . import views

app_name = 'lares_temporarios'

urlpatterns = [
    path('', views.GatoListView.as_view(), name='lista'),
    path('gato/<int:pk>/', views.GatoDetailView.as_view(), name='detail'),
    path('solicitar/', views.formulario_lar_temporario, name='formulario_lar_temporario'),
    path('obrigado/', views.LarTemporarioSuccessView.as_view(), name='lar_temporario_sucess'),
]