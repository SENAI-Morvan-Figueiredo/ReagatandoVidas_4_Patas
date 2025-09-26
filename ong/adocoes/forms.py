from django import forms
from .models import Adocao ##, Adotados

class AdocaoForm(forms.ModelForm):
    class Meta:
        model = Adocao
        fields = '__all__'

# class AdotadosForm(forms.ModelForm):
#     model = Adotados