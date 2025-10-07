from django.contrib import admin
from .models import Adocao, Adotados

# Register your models here.

admin.site.register(Adotados)
admin.site.register(Adocao)