# adocoes/forms.py
from django import forms
from .models import Adocao

class AdocaoForm(forms.ModelForm):
    class Meta:
        model = Adocao
        exclude = ['created_at', 'updated_at']  
        widgets = {
            'codicoes_financeiras': forms.CheckboxInput(),
            'animal_externo': forms.CheckboxInput(),
            'periodo_adaptacao': forms.CheckboxInput(),
            # adicione outros booleanos como CheckboxInput
            'rua': forms.TextInput(attrs={'class': 'form-control'}),
            'bairro': forms.TextInput(attrs={'class': 'form-control'}),
            'numero': forms.TextInput(attrs={'class': 'form-control'}),
            'cidade': forms.TextInput(attrs={'class': 'form-control'}),
            'cep': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'numero_contato': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '11999998888'}),
            'instagram': forms.TextInput(attrs={'class': 'form-control'}),
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'idade': forms.NumberInput(attrs={'class': 'form-control'}),
            'ocupacao_profissional': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_numero_contato(self):
        num = self.cleaned_data.get('numero_contato', '')
        only_digits = ''.join(c for c in num if c.isdigit())
        if len(only_digits) < 10:
            raise forms.ValidationError("Número de contato inválido.")
        return only_digits