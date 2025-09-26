from django.db import models
from gatos.models import Gato


class Adocao(models.Model):
  
    # Informações do adotante
    gato = models.ForeignKey(Gato, on_delete=models.CASCADE, verbose_name="Gato")##p/ teste de formulario:
    nome = models.CharField(max_length=255, verbose_name="Nome")
    idade = models.IntegerField(verbose_name="Idade")
    ocupacao_profissional = models.CharField(max_length=100, verbose_name="Ocupação profissional")
    email = models.EmailField(max_length=255, verbose_name="Email")
    codicoes_financeiras = models.BooleanField(default=False, verbose_name="Capacidade de arcar com os custos do gato")
    
    # Endereço
    rua = models.CharField(max_length=150, verbose_name="Rua")
    bairro = models.CharField(max_length=150, verbose_name="Bairro")
    numero = models.CharField(max_length=6, verbose_name="Número")
    cidade = models.CharField(max_length=150, verbose_name="Cidade")
    cep = models.IntegerField(verbose_name="CEP")
    
    # Contato e redes sociais
    instagram = models.CharField(max_length=100, blank=True, null=True, verbose_name="Instagram")
    numero_contato = models.CharField(max_length=11, verbose_name="Número de contato")
    
    # Informações sobre outros animais
    animal_externo = models.BooleanField(default=False, verbose_name="Possui outros animais")
    animal_externo_voltinhas = models.BooleanField(default=False, blank=True, null=True, verbose_name="Animais costumam dar voltinhas na rua")
    animal_externo_especie_idade = models.TextField(blank=True, null=True, verbose_name="Espécie e idades dos animais")
    animal_externo_nao_castrado = models.BooleanField(default=False, blank=True, null=True, verbose_name="Possui algum gato não castrado")
    animal_externo_vacinacao = models.BooleanField(default=False, blank=True, null=True, verbose_name="Opinião sobre vacinação")
    animal_externo_testado = models.BooleanField(default=False, blank=True, null=True, verbose_name="Animais testados para Fiv e FeLV")
    animal_externo_racao = models.TextField(blank=True, null=True, verbose_name="Ração usada para os pets")
    
    # Informações sobre adaptação
    periodo_adaptacao = models.BooleanField(default=False, verbose_name="Ciente do período de adaptação")
    
    # Informações sobre moradia
    mora_sozinho = models.BooleanField(default=False, verbose_name="Mora sozinho")
    mora_crianca = models.BooleanField(default=False, blank=True, null=True, verbose_name="Moram crianças na casa")
    alguem_nao_concorda = models.BooleanField(default=False, blank=True, null=True, verbose_name="Alguém da família não concorda")
    alguem_alergico = models.BooleanField(default=False, blank=True, null=True, verbose_name="Alguém tem alergia")
    imovel_proprio = models.BooleanField(default=False, verbose_name="Imóvel próprio")
    mora_casa = models.BooleanField(default=False, verbose_name="Mora em uma casa")
    
    # Características da moradia
    casa_muros_laterais_baixos = models.BooleanField(default=False, blank=True, null=True, verbose_name="Muros laterais e fundos são baixos")
    casa_quintal = models.BooleanField(default=False, blank=True, null=True, verbose_name="Possui quintal")
    casa_quintal_mais_casa = models.BooleanField(default=False, blank=True, null=True, verbose_name="Possui mais casas no quintal")
    casa_garagem = models.BooleanField(default=False, blank=True, null=True, verbose_name="Gato terá acesso à garagem")
    apartamento_telada = models.BooleanField(default=False, blank=True, null=True, verbose_name="Possui tela nas janelas e sacada do apartamento")
    apartamento_limitador = models.BooleanField(default=False, blank=True, null=True, verbose_name="Janelas do banheiro têm limitador")
    
    # Mudanças e estabilidade
    mudanca_trabalho = models.BooleanField(default=False, verbose_name="Em caso de mudança de trabalho, ainda terá responsabilidade")
    mudanca_imovel = models.BooleanField(default=False, verbose_name="Tem vontade de mudar de imóvel")
    mudanca_imovel_seguranca = models.BooleanField(default=False, verbose_name="Se mudar de imóvel, manterá a segurança")
    mudanca_imovel_comunicar = models.BooleanField(default=False, verbose_name="Se mudar de imóvel, comunicará a ONG")
    
    # Compromissos e responsabilidades
    repassar_animal = models.BooleanField(default=False, verbose_name="Não pode repassar o animal para outra pessoa")
    dessistencia = models.BooleanField(default=False, verbose_name="Em caso de desistência, a ONG deve ser avisada")
    viagens = models.TextField(verbose_name="Em viagens, quem ficará com o animal")
    restrito = models.BooleanField(default=False, verbose_name="Animal ficará restrito na residência")
    devolver_doar = models.BooleanField(default=False, verbose_name="Já entregou animal para ONG ou Zoonoses")
    devolver_doar_explique = models.TextField(blank=True, null=True, verbose_name="Explicar situação do incidente de devolução/doação")
    responder_doador = models.BooleanField(default=False, verbose_name="Compromisso em atualizar o doador sobre o animal")
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Atualizado em")
    
    class Meta:
        verbose_name = "Adoção"
        verbose_name_plural = "Adoções"
        db_table = "adocao"
        ordering = ["-created_at"]
    
    def __str__(self):
        return f"{self.nome} - {self.gato.nome}"

class Adotados(models.Model):
    imagem = models.ImageField(upload_to="gatos/", verbose_name="Imagem")
    gato = models.ForeignKey(Gato, on_delete=models.CASCADE, verbose_name="Gato")
    adocao = models.ForeignKey(Adocao, on_delete=models.CASCADE, verbose_name="Adoção")
    data_inicio = models.DateField(verbose_name="Data de início")

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Atualizado em")
    
    class Meta:
        verbose_name = "Adotado"
        verbose_name_plural = "Adotados"
        db_table = "adotados"
        ordering = ["-created_at"]
    
    def __str__(self):
        return f"{self.gato}"