from django import forms
from .models import Gato

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
        fields = "__all__"  # inclui todos os campos do model

        widgets = {
            # ---------------- BOOLEANOS (Sim / Não) ----------------
            'lar_temporario': forms.RadioSelect(choices=SIM_NAO_CHOICES),
            'sexo': forms.RadioSelect(choices=SEXO_CHOICES),

            # -------- Campos de texto --------
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'idade': forms.TextInput(attrs={'class': 'form-control'}),

             # -------- Imagem --------
            'imagem': forms.TextInput(attrs={'class': 'form-control'}),

            # -------- TextArea --------
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }