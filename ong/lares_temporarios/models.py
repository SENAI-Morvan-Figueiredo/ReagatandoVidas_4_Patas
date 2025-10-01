from django.db import models
from gatos.models import Gato


class LarTemporario(models.Model):
    gato = models.ForeignKey(Gato, on_delete=models.CASCADE, verbose_name="Gato", null=True, blank=True)
    nome = models.CharField(max_length=255, verbose_name="Nome")
    cpf = models.CharField(max_length=14, verbose_name="CPF")
    ocupacao_profissional = models.CharField(max_length=255, verbose_name="Ocupação profissional")
    rua = models.CharField(max_length=255, verbose_name="Rua")
    bairro = models.CharField(max_length=255, verbose_name="Bairro")
    numero = models.CharField(max_length=15, verbose_name="Número")
    cidade = models.CharField(max_length=255, verbose_name="Cidade")
    cep = models.IntegerField(verbose_name="CEP") 
    numero_contato = models.CharField(max_length=15, verbose_name="Número de contato")
    foi_lar_temporario = models.BooleanField(default=False, verbose_name="Já foi lar temporário")
    disponibilidade_inicio = models.DateField(verbose_name="Disponibilidade início")
    animal_externo = models.TextField(verbose_name="Possui outros animais (descrição)")
    mora_casa = models.BooleanField(default=False, verbose_name="Mora em casa")
    restrito = models.BooleanField(default=False, verbose_name="Gato ficará restrito em alguma parte da casa")
    estrutura = models.CharField(max_length=20, verbose_name="Tem estrutura segura para gatos")
    custos = models.CharField(max_length=50, verbose_name="Pode ajudar com os custos do gato")
    duracao_aproximada = models.CharField(max_length=20, verbose_name="Por quanto tempo consegue manter o gato")
    visita = models.CharField(max_length=50, verbose_name="Aceita visita em caso de adoção")
    informacao_adicional = models.TextField(blank=True, null=True, verbose_name="Informação adicional do voluntário")
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Atualizado em")
    
    class Meta:
        verbose_name = "Lar Temporário"
        verbose_name_plural = "Lares Temporários"
        db_table = "lar_temporario"
        ordering = ["-created_at"]
    
    def __str__(self):
        return f"{self.nome} - {self.bairro}, {self.cidade}"

class HistoricoLarTemporario(models.Model):
    gato = models.ForeignKey(Gato, on_delete=models.CASCADE, verbose_name="Gato")
    lar_temporario = models.ForeignKey(LarTemporario, on_delete=models.CASCADE, verbose_name="Lar temporário")
    data_inicio = models.DateField(verbose_name="Data de início")
    data_fim = models.DateField(blank=True, null=True, verbose_name="Data de fim")
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Atualizado em")
    
    class Meta:
        verbose_name = "Histórico de Lar Temporário"
        verbose_name_plural = "Históricos de Lares Temporários"
        db_table = "historico_lar_temporario"
        ordering = ["-data_inicio"]
    
    def __str__(self):
        return f"{self.gato.nome} - {self.lar_temporario.nome}"

class LarTemporarioAtual(models.Model):
    gato = models.ForeignKey(Gato, on_delete=models.CASCADE, verbose_name="Gato")
    lar_temporario = models.ForeignKey(LarTemporario, on_delete=models.CASCADE, verbose_name="Lar temporário")
    data_inicio = models.DateField(verbose_name="Data de início")

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Atualizado em")
    
    class Meta:
        verbose_name = "Lar Temporario Atual"
        verbose_name_plural = "Lares Temporários Atuais"
        db_table = "lar_temporario_atual"
        ordering = ["-data_inicio"]
    
    def __str__(self):
        return f"{self.gato.nome} - {self.lar_temporario.nome}"