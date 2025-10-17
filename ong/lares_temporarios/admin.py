from django.contrib import admin
from .models import LarTemporario, HistoricoLarTemporario, LarTemporarioAtual
# Register your models here.

admin.site.register(LarTemporario)
admin.site.register(HistoricoLarTemporario)
admin.site.register(LarTemporarioAtual)