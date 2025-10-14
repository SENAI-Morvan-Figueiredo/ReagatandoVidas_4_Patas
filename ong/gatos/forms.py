from django import forms
from .models import Gato, Cuidado, Temperamento, Sociavel, Moradia

SIM_NAO_CHOICES = [
    (True, "Sim"),
    (False, "Não"),
]

SEXO_CHOICES = [
        ("M", "Macho"),
        ("F", "Fêmea"),
    ]


class GatoForm(forms.ModelForm):
    class Meta:
        model = Gato
        fields = "__all__" 

        widgets = {
            # ---------------- BOOLEANOS----------------
            'lar_temporario': forms.RadioSelect(choices=SIM_NAO_CHOICES),
            'sexo': forms.RadioSelect(choices=SEXO_CHOICES),

            # -------- Campos de texto --------
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'idade': forms.TextInput(attrs={'class': 'form-control'}),

            # -------- Imagem --------
            'imagem': forms.FileInput(attrs={'class': 'form-control-file', 'accept': 'image/*'}),

            # -------- TextArea --------
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class CuidadoForm(forms.ModelForm):
    class Meta:
        model = Cuidado
        fields = "__all__" 

        widgets = {
            'castrado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'vacinado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'vermifugado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'cuidado_especial': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'fiv_negativo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'fiv_positivo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'felv_negativo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'felv_positivo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class TemperamentoForm(forms.ModelForm):
    class Meta:
        model = Temperamento
        fields = '__all__'

        widgets = {
        'docil': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'agressivo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'calmo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'brincalhao': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'arisco': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'independente': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'carente': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
    }

class MoradiaForm(forms.ModelForm):
    class Meta:
        model = Moradia
        fields = '__all__'
        widgets = {
        'casa_com_quintal': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'apartamento': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
    }

class SociavelForm(forms.ModelForm):
    class Meta:
        model = Sociavel
        fields = '__all__'

        widgets = {
        'gatos': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'desconhecidos': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'cachorros': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'criancas': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'nao_sociavel': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
    }