from django.contrib import admin
from .models import Gato, Temperamento, Sociavel, Cuidado, Moradia

admin.site.register(Gato)
admin.site.register(Temperamento)
admin.site.register(Sociavel)
admin.site.register(Cuidado)
admin.site.register(Moradia)
