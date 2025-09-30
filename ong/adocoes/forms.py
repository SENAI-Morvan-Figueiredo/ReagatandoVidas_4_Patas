# adocoes/forms.py
from django import forms
from .models import Adocao


class AdocaoForm(forms.ModelForm):
    class Meta:
        model = Adocao
        fields = "__all__"  # inclui todos os campos do model

        widgets = {
            # ---------------- BOOLEANOS (Sim / Não) ----------------
            'codicoes_financeiras': forms.RadioSelect(choices=[(True, "Sim"), (False, "Não")]),
            'animal_externo': forms.RadioSelect(choices=[(True, "Sim"), (False, "Não")]),
            'animal_externo_voltinhas': forms.RadioSelect(choices=[(True, "Sim"), (False, "Não")]),
            'animal_externo_nao_castrado': forms.RadioSelect(choices=[(True, "Sim"), (False, "Não")]),
            'animal_externo_vacinacao': forms.RadioSelect(choices=[(True, "Sim"), (False, "Não")]),
            'animal_externo_testado': forms.RadioSelect(choices=[(True, "Sim"), (False, "Não")]),
            'periodo_adaptacao': forms.RadioSelect(choices=[(True, "Sim"), (False, "Não")]),
            'mora_sozinho': forms.RadioSelect(choices=[(True, "Sim"), (False, "Não")]),
            'mora_crianca': forms.RadioSelect(choices=[(True, "Sim"), (False, "Não")]),
            'alguem_nao_concorda': forms.RadioSelect(choices=[(True, "Sim"), (False, "Não")]),
            'alguem_alergico': forms.RadioSelect(choices=[(True, "Sim"), (False, "Não")]),
            'imovel_proprio': forms.RadioSelect(choices=[(True, "Sim"), (False, "Não")]),
            'mora_casa': forms.RadioSelect(choices=[(True, "Sim"), (False, "Não")]),
            'casa_muros_laterais_baixos': forms.RadioSelect(choices=[(True, "Sim"), (False, "Não")]),
            'casa_quintal': forms.RadioSelect(choices=[(True, "Sim"), (False, "Não")]),
            'casa_quintal_mais_casa': forms.RadioSelect(choices=[(True, "Sim"), (False, "Não")]),
            'casa_garagem': forms.RadioSelect(choices=[(True, "Sim"), (False, "Não")]),
            'apartamento_telada': forms.RadioSelect(choices=[(True, "Sim"), (False, "Não")]),
            'apartamento_limitador': forms.RadioSelect(choices=[(True, "Sim"), (False, "Não")]),
            'mudanca_trabalho': forms.RadioSelect(choices=[(True, "Sim"), (False, "Não")]),
            'mudanca_imovel': forms.RadioSelect(choices=[(True, "Sim"), (False, "Não")]),
            'mudanca_imovel_seguranca': forms.RadioSelect(choices=[(True, "Sim"), (False, "Não")]),
            'mudanca_imovel_comunicar': forms.RadioSelect(choices=[(True, "Sim"), (False, "Não")]),
            'repassar_animal': forms.RadioSelect(choices=[(True, "Sim"), (False, "Não")]),
            'dessistencia': forms.RadioSelect(choices=[(True, "Sim"), (False, "Não")]),
            'restrito': forms.RadioSelect(choices=[(True, "Sim"), (False, "Não")]),
            'devolver_doar': forms.RadioSelect(choices=[(True, "Sim"), (False, "Não")]),
            'responder_doador': forms.RadioSelect(choices=[(True, "Sim"), (False, "Não")]),

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
            raise forms.ValidationError("Número de contato inválido.")
        return only_digits
