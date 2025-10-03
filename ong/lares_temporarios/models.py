from django.db import models
from gatos.models import Gato


class LarTemporario(models.Model):
    # Informações do adotante
    gato = models.ForeignKey(Gato, on_delete=models.CASCADE, verbose_name="Gato", null=True, blank=True)
    nome = models.CharField(max_length=255, verbose_name="Nome Completo")
    cpf = models.CharField(max_length=14, verbose_name="CPF")
    ocupacao_profissional = models.CharField(max_length=255, verbose_name="Ocupação profissional")
    email = models.EmailField(max_length=255, verbose_name="E-mail")

    # Endereço
    rua = models.CharField(max_length=255, verbose_name="Rua")
    bairro = models.CharField(max_length=255, verbose_name="Bairro")
    numero = models.CharField(max_length=15, verbose_name="Número")
    cidade = models.CharField(max_length=255, verbose_name="Cidade")
    cep = models.IntegerField(verbose_name="CEP") 

    # Contato
    numero_contato = models.CharField(max_length=15, verbose_name="Telefone para contato")

    # Lar Temporário
    foi_lar_temporario = models.BooleanField(default=False, verbose_name="Você já foi lar temporário antes?")
    disponibilidade_inicio = models.DateField(verbose_name="Informe uma data em que se inicia a sua disponibilidade para ser lar temporário de um bichinho")
    animal_externo = models.TextField(verbose_name="Você tem outros animais em casa? Se sim, quantos e quais?  Caso ele tenha alguma condição como FIV, FELV, esporotricose etc, nos informe aqui também!")
    mora_casa = models.BooleanField(default=False, verbose_name="Mora em casa?")
    restrito = models.BooleanField(default=False, verbose_name="O animal ficará restrito em alguma parte da casa?")
    estrutura = models.CharField(max_length=20, verbose_name="Você tem estrutura segura para gatos (telas nas janelas, ambiente fechado etc)?")
    custos = models.CharField(max_length=50, verbose_name="Você pode ajudar com os custos (ração, areia, etc), ou prefere que a Resgatando vidas 4 patas cubra?")
    duracao_aproximada = models.CharField(max_length=20, verbose_name="Por quanto tempo, aproximadamente, você conseguiria manter um animalzinho sob seus cuidados?  ")
    visita = models.CharField(max_length=50, verbose_name="Caso haja um adotante interessado em visitar o animalzinho, você poderá recebê-lo?")
    informacao_adicional = models.TextField(blank=True, null=True, verbose_name="Alguma observação ou informação que gostaria de adicionar?")
    
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