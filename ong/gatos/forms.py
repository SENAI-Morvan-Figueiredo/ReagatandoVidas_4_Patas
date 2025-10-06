from django import forms
from .models import Gato, Temperamento, Sociavel, Cuidado, Moradia

SIM_NAO_CHOICES = [
    (True, "Sim"),
    (False, "Não"),
]

class GatoForm(forms.ModelForm):
    class Meta:
        model = Gato
        fields = ['nome', 'sexo', 'idade', 'lar_temporario', 'descricao', 'imagem', 
                 'cuidado', 'temperamento', 'sociavel', 'moradia']

        widgets = {
            # Campos de texto
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o nome do gato'
            }),
            'idade': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: 2 anos'
            }),
            
            # Radio buttons
            'sexo': forms.RadioSelect(attrs={'class': 'radio-group'}),
            'lar_temporario': forms.RadioSelect(
                choices=SIM_NAO_CHOICES,
                attrs={'class': 'radio-group'}
            ),

            # TextArea
            'descricao': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Conte mais sobre o gato...'
            }),

            # Upload de imagem
            'imagem': forms.FileInput(attrs={
                'class': 'form-control-file',
                'accept': 'image/*'
            }),
            
            # Campos relacionados - serão renderizados como hidden por enquanto
            'cuidado': forms.HiddenInput(),
            'temperamento': forms.HiddenInput(),
            'sociavel': forms.HiddenInput(),
            'moradia': forms.HiddenInput(),
        }

        labels = {
            'nome': 'Nome do gato',
            'sexo': 'Sexo',
            'idade': 'Idade',
            'lar_temporario': 'Lar Temporário',
            'descricao': 'Sobre o gato',
            'imagem': 'Foto do gato',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Adicionar classes CSS aos campos
        for field_name, field in self.fields.items():
            if field_name not in ['sexo', 'lar_temporario', 'cuidado', 'temperamento', 'sociavel', 'moradia']:
                field.widget.attrs.update({'class': 'form-control'})

    def save(self, commit=True):
        instance = super().save(commit=False)
        
        if commit:
            # Criar instâncias dos modelos relacionados com base nos dados do formulário
            
            # Criar Temperamento
            temperamento = Temperamento.objects.create()
            instance.temperamento = temperamento
            
            # Criar Sociavel
            sociavel = Sociavel.objects.create()
            instance.sociavel = sociavel
            
            # Criar Cuidado
            cuidado = Cuidado.objects.create()
            instance.cuidado = cuidado
            
            # Criar Moradia
            moradia = Moradia.objects.create()
            instance.moradia = moradia
            
            instance.save()
            
        return instance


# Forms separados para os modelos relacionados
class TemperamentoForm(forms.ModelForm):
    class Meta:
        model = Temperamento
        fields = ['docil', 'agressivo', 'calmo', 'brincalhao', 'arisco', 'independente', 'carente']
        widgets = {
            'docil': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'agressivo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'calmo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'brincalhao': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'arisco': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'independente': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'carente': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class SociavelForm(forms.ModelForm):
    class Meta:
        model = Sociavel
        fields = ['gatos', 'desconhecidos', 'cachorros', 'criancas', 'nao_sociavel']
        widgets = {
            'gatos': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'desconhecidos': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'cachorros': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'criancas': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'nao_sociavel': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class CuidadoForm(forms.ModelForm):
    class Meta:
        model = Cuidado
        fields = ['castrado', 'vacinado', 'vermifugado', 'cuidado_especial', 
                 'fiv_negativo', 'fiv_positivo', 'felv_negativo', 'felv_positivo']
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

class MoradiaForm(forms.ModelForm):
    class Meta:
        model = Moradia
        fields = ['casa_com_quintal', 'apartamento']
        widgets = {
            'casa_com_quintal': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'apartamento': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


# Form combinado que inclui todos os formulários
class GatoCompletoForm:
    def __init__(self, data=None, files=None, instance=None):
        self.gato_form = GatoForm(data=data, files=files, instance=instance)
        
        # Se estamos editando um gato existente, carregar os dados dos modelos relacionados
        if instance:
            self.temperamento_form = TemperamentoForm(data=data, instance=instance.temperamento)
            self.sociavel_form = SociavelForm(data=data, instance=instance.sociavel)
            self.cuidado_form = CuidadoForm(data=data, instance=instance.cuidado)
            self.moradia_form = MoradiaForm(data=data, instance=instance.moradia)
        else:
            self.temperamento_form = TemperamentoForm(data=data)
            self.sociavel_form = SociavelForm(data=data)
            self.cuidado_form = CuidadoForm(data=data)
            self.moradia_form = MoradiaForm(data=data)
    
    def is_valid(self):
        return (self.gato_form.is_valid() and 
                self.temperamento_form.is_valid() and 
                self.sociavel_form.is_valid() and 
                self.cuidado_form.is_valid() and 
                self.moradia_form.is_valid())
    
    def save(self, commit=True):
        if not self.is_valid():
            raise ValueError("Formulário inválido")
        
        # Salvar os modelos relacionados primeiro
        temperamento = self.temperamento_form.save(commit=commit)
        sociavel = self.sociavel_form.save(commit=commit)
        cuidado = self.cuidado_form.save(commit=commit)
        moradia = self.moradia_form.save(commit=commit)
        
        # Salvar o gato com as referências
        gato = self.gato_form.save(commit=False)
        gato.temperamento = temperamento
        gato.sociavel = sociavel
        gato.cuidado = cuidado
        gato.moradia = moradia
        
        if commit:
            gato.save()
        
        return gato

