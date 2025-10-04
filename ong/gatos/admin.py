from django.contrib import admin
from .models import Gato, Moradia, Temperamento, Sociavel, Cuidado

# Registrando os Models para que SuperAdmin possa adicionar, editar e etc.

admin.site.register(Gato)
admin.site.register(Moradia)
admin.site.register(Temperamento)
admin.site.register(Sociavel)
admin.site.register(Cuidado)