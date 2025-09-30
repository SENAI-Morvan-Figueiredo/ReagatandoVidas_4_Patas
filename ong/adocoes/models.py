from django.db import models
from gatos.models import Gato


class Adocao(models.Model):
  
    # Informações do adotante
    gato = models.ForeignKey(Gato, on_delete=models.CASCADE, verbose_name="Gato")
    nome = models.CharField(max_length=255, verbose_name="Nome Completo")
    cpf = models.CharField(max_length=14, verbose_name="CPF")
    idade = models.IntegerField(verbose_name="Idade")
    ocupacao_profissional = models.CharField(max_length=100, verbose_name="Ocupação profissional")
    email = models.EmailField(max_length=255, verbose_name="E-mail")
    codicoes_financeiras = models.BooleanField(default=False, verbose_name="Está em condições financeiras de arcar com ração de qualidade, custos veterinários como consultas, vacinas, exames e tratamentos sempre que necessário?")
    
    # Endereço
    rua = models.CharField(max_length=150, verbose_name="Rua")
    bairro = models.CharField(max_length=150, verbose_name="Bairro")
    numero = models.CharField(max_length=6, verbose_name="Número")
    cidade = models.CharField(max_length=150, verbose_name="Cidade")
    cep = models.IntegerField(verbose_name="CEP")
    
    # Contato e redes sociais
    instagram = models.CharField(max_length=100, blank=True, null=True, verbose_name="Qual seu usuário no Instagram?")
    numero_contato = models.CharField(max_length=11, verbose_name="Telefone para contato")
    
    # Informações sobre outros animais
    animal_externo = models.BooleanField(default=False, verbose_name="Possui outros animais?")
    animal_externo_voltinhas = models.BooleanField(default=False, blank=True, null=True, verbose_name="Seus animais são acostumados a darem voltinhas na rua ou casas vizinhas?")
    animal_externo_especie_idade = models.TextField(blank=True, null=True, verbose_name="Quais bichinhos possui atualmente? (espécie e idade)")
    animal_externo_nao_castrado = models.BooleanField(default=False, blank=True, null=True, verbose_name="Tem algum gato que ainda não foi castrado? ")
    animal_externo_vacinacao = models.BooleanField(default=False, blank=True, null=True, verbose_name="Você acha importante manter as vacinações em dia? ")
    animal_externo_testado = models.BooleanField(default=False, blank=True, null=True, verbose_name="Para gatos;  São testados para Fiv e Felv?")
    animal_externo_racao = models.TextField(blank=True, null=True, verbose_name="Qual ração você oferece para seus cães e gatos?")
    
    # Informações sobre adaptação
    periodo_adaptacao = models.BooleanField(default=False, verbose_name="Está ciente que no período de adaptação o bichinho recém- chegado precisará estar em um quarto com algum membro da família, para que não fique sozinho e que não tenha contato imediato, sem a devida adaptação, com os outros bichinhos da casa?")
    
    # Informações sobre moradia
    mora_sozinho = models.BooleanField(default=False, verbose_name="Você mora sozinho?:")
    mora_crianca = models.BooleanField(default=False, blank=True, null=True, verbose_name="Moram crianças (até 12 anos)?")
    alguem_nao_concorda = models.BooleanField(default=False, blank=True, null=True, verbose_name="Tem algum membro da família que não concorde com a adoção")
    alguem_alergico = models.BooleanField(default=False, blank=True, null=True, verbose_name="Tem alguma criança ou membro da família com sintomas alérgicos?")
    imovel_proprio = models.BooleanField(default=False, verbose_name="Seu imóvel é próprio?")
    mora_casa = models.BooleanField(default=False, verbose_name="Mora em uma casa?")
    
    # Características da moradia
    casa_muros_laterais_baixos = models.BooleanField(default=False, blank=True, null=True, verbose_name="Muros laterais e fundos são baixo?")
    casa_quintal = models.BooleanField(default=False, blank=True, null=True, verbose_name="Possui quintal?")
    casa_quintal_mais_casa = models.BooleanField(default=False, blank=True, null=True, verbose_name="Possui mais casas no quintal?")
    casa_garagem = models.BooleanField(default=False, blank=True, null=True, verbose_name="Gato terá acesso à garagem?")
    apartamento_telada = models.BooleanField(default=False, blank=True, null=True, verbose_name="Possui tela nas janelas e sacada do apartamento?")
    apartamento_limitador = models.BooleanField(default=False, blank=True, null=True, verbose_name="Janelas do banheiro têm limitador?")
    
    # Mudanças e estabilidade
    mudanca_trabalho = models.BooleanField(default=False, verbose_name="Tem perspectivas de mudança de trabalho, cidade, Estado ou País que comprometa a sua responsabilidade com esse animal a longo prazo?")
    mudanca_imovel = models.BooleanField(default=False, verbose_name="Tem perspectiva de mudança de imóvel?")
    mudanca_imovel_seguranca = models.BooleanField(default=False, verbose_name="No caso de mudança de imóvel, você tem ciência que o novo imóvel deverá ser totalmente telado antes da efetiva mudança mantendo assim a mesma segurança para o gatinho?")
    mudanca_imovel_comunicar = models.BooleanField(default=False, verbose_name="No caso de mudança de imóvel, você se responsabiliza a comunicar o doador do novo endereço e da mesma forma, enviar vídeo comprovando a segurança do novo imóvel para o gatinho?")
    
    # Compromissos e responsabilidades
    repassar_animal = models.BooleanField(default=False, verbose_name="Está ciente que não pode repassar esse animal para outra pessoa seja por forma de doação ou presente?")
    dessistencia = models.BooleanField(default=False, verbose_name="Em caso de desistência por força maior, está ciente que será obrigado a comunicar o doador para que o mesmo encontre um novo lar para o animal, e que nesse período, continuará cuidando, alimentando e provendo toda segurança, até que seja encontrado um novo lar para ele (caso o doador não consiga recebe-lo de imediato)?")
    viagens = models.TextField(verbose_name="Em ocasiões de viagens, quem seria a pessoa que ficaria responsável em ir até o seu imóvel para cuidar da higiene e alimentação do(s) seu(s) animais(s)?")
    restrito = models.BooleanField(default=False, verbose_name="O animal ficará restrito em alguma parte da casa?")
    devolver_doar = models.BooleanField(default=False, verbose_name="Você já precisou doar, devolver ou entregar na Zoonoses ou Ongs algum gato ou cachorro seu?")
    devolver_doar_explique = models.TextField(blank=True, null=True, verbose_name="Se sim, nos conte o que aconteceu?")
    responder_doador = models.BooleanField(default=False, verbose_name="Você tem alguma objeção em responder o doador sobre a adaptação e condições de vida e saúde do animal adotado sempre que esse achar necessário?")
    
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