from django.contrib import admin
from .models import Gato, Moradia, Temperamento, Sociavel, Cuidado

# Register your models here.

admin.site.register(Gato)
admin.site.register(Moradia)
admin.site.register(Temperamento)
admin.site.register(Sociavel)
admin.site.register(Cuidado)