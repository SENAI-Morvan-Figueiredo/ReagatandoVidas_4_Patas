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
    sexo = forms.TypedChoiceField(
        choices=Gato.SEXO_CHOICES,
        widget=forms.RadioSelect,
        coerce=str,
        empty_value=None
    )

    class Meta:
        model = Gato
        exclude = ['cuidado', 'temperamento', 'sociavel', 'moradia']  # <-- trocado
        widgets = {
            'lar_temporario': forms.RadioSelect(choices=SIM_NAO_CHOICES),
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'idade': forms.TextInput(attrs={'class': 'form-control'}),
            'imagem': forms.FileInput(attrs={'class': 'form-control-file', 'accept': 'image/*'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['sexo'].empty_label = None


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
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False

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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False


class MoradiaForm(forms.ModelForm):
    class Meta:
        model = Moradia
        fields = '__all__'
        widgets = {
            'casa_com_quintal': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'apartamento': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False


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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False
        
        
        
        
# class LarTemporarioForm(forms.ModelForm):
#     class Meta:
#         model = LarTemporario
#         fields = '__all__'

#         widgets = {
#         'nome': forms.TextInput(attrs={'class': 'form-control'}),
#         'disponibilidade_inicio': forms.DateField(attrs={'class': 'form-control'}),
#     }