# administrador/admin.py

from django.contrib import admin
from .models import Adminstrador  # Importe seu modelo

# Crie uma classe para personalizar a exibição no admin (opcional, mas recomendado)
class AdminstradorAdmin(admin.ModelAdmin):
    # Mostra estes campos na lista de administradores
    list_display = ('email', 'id') 
    
    # Adiciona um campo de busca para facilitar encontrar usuários
    search_fields = ('email',)

# Registre seu modelo com a classe de personalização
admin.site.register(Adminstrador, AdminstradorAdmin)
