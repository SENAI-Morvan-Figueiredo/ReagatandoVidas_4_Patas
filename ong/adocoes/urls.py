from django.urls import path
from .views import nova_adocao , lista_adocoes

urlpatterns = [
    path('nova/', nova_adocao, name='nova_adocao'),
    path('lista/', lista_adocoes, name='lista_adocoes'),
]