from django.urls import path
from .views import nova_adocao

urlpatterns = [
    path('nova/', nova_adocao, name='nova_adocao'),
]