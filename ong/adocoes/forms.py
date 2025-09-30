# adocoes/forms.py
from django import forms
from .models import Adocao

SIM_NAO_CHOICES = [
    (True, "Sim"),
    (False, "Não"),
]

class AdocaoForm(forms.ModelForm):
    class Meta:
        model = Adocao
        fields = "__all__"  # inclui todos os campos do model

        widgets = {
            # ---------------- BOOLEANOS (Sim / Não) ----------------
            'codicoes_financeiras': forms.RadioSelect(choices=SIM_NAO_CHOICES),
            'animal_externo': forms.RadioSelect(choices=SIM_NAO_CHOICES),
            'animal_externo_voltinhas': forms.RadioSelect(choices=SIM_NAO_CHOICES),
            'animal_externo_nao_castrado': forms.RadioSelect(choices=SIM_NAO_CHOICES),
            'animal_externo_vacinacao': forms.RadioSelect(choices=SIM_NAO_CHOICES),
            'animal_externo_testado': forms.RadioSelect(choices=SIM_NAO_CHOICES),
            'periodo_adaptacao': forms.RadioSelect(choices=SIM_NAO_CHOICES),
            'mora_sozinho': forms.RadioSelect(choices=SIM_NAO_CHOICES),
            'mora_crianca': forms.RadioSelect(choices=SIM_NAO_CHOICES),
            'alguem_nao_concorda': forms.RadioSelect(choices=SIM_NAO_CHOICES),
            'alguem_alergico': forms.RadioSelect(choices=SIM_NAO_CHOICES),
            'imovel_proprio': forms.RadioSelect(choices=SIM_NAO_CHOICES),
            'mora_casa': forms.RadioSelect(choices=SIM_NAO_CHOICES),
            'casa_muros_laterais_baixos': forms.RadioSelect(choices=SIM_NAO_CHOICES),
            'casa_quintal': forms.RadioSelect(choices=SIM_NAO_CHOICES),
            'casa_quintal_mais_casa': forms.RadioSelect(choices=SIM_NAO_CHOICES),
            'casa_garagem': forms.RadioSelect(choices=SIM_NAO_CHOICES),
            'apartamento_telada': forms.RadioSelect(choices=SIM_NAO_CHOICES),
            'apartamento_limitador': forms.RadioSelect(choices=SIM_NAO_CHOICES),
            'mudanca_trabalho': forms.RadioSelect(choices=SIM_NAO_CHOICES),
            'mudanca_imovel': forms.RadioSelect(choices=SIM_NAO_CHOICES),
            'mudanca_imovel_seguranca': forms.RadioSelect(choices=SIM_NAO_CHOICES),
            'mudanca_imovel_comunicar': forms.RadioSelect(choices=SIM_NAO_CHOICES),
            'repassar_animal': forms.RadioSelect(choices=SIM_NAO_CHOICES),
            'dessistencia': forms.RadioSelect(choices=SIM_NAO_CHOICES),
            'restrito': forms.RadioSelect(choices=SIM_NAO_CHOICES),
            'devolver_doar': forms.RadioSelect(choices=SIM_NAO_CHOICES),
            'responder_doador': forms.RadioSelect(choices=SIM_NAO_CHOICES),

            # ---------------- CAMPOS DE TEXTO / NÚMERO ----------------
            'rua': forms.TextInput(attrs={'class': 'form-control'}),
            'bairro': forms.TextInput(attrs={'class': 'form-control'}),
            'numero': forms.TextInput(attrs={'class': 'form-control'}),
            'cidade': forms.TextInput(attrs={'class': 'form-control'}),
            'cep': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'numero_contato': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '11999998888'}),
            'instagram': forms.TextInput(attrs={'class': 'form-control'}),
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control'}),
            'idade': forms.NumberInput(attrs={'class': 'form-control'}),
            'ocupacao_profissional': forms.TextInput(attrs={'class': 'form-control'}),

            # ---------------- TEXTAREAS (respostas longas) ----------------
            'animal_externo_especie_idade': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'animal_externo_racao': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'viagens': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'devolver_doar_explique': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }

    def clean_numero_contato(self):
        num = self.cleaned_data.get('numero_contato', '')
        only_digits = ''.join(c for c in num if c.isdigit())
        if len(only_digits) < 10:
            raise forms.ValidationError("Número de contato inválido. Informe DDD + número.")
        return only_digits