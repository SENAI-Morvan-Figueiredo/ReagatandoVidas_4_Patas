import logging
from django.views.generic import CreateView
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from gatos.models import Gato
from lares_temporarios.models import LarTemporarioAtual
from adocoes.models import Adotados
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from .forms import GatoForm, CuidadoForm, TemperamentoForm, SociavelForm, MoradiaForm
from django.urls import reverse_lazy
from django.db.models import Q


# ---------------------------------------------------------------------------------------- Da tela dashboard_admin_adocoes

# View que vai mandar as informações para os cards e tambem para o filtro
def dashboard_admin_adocoes(request):
    # Pega todos os gatos
    gatos = Gato.objects.all()

    # Excluir gatos que já foram adotados
    gatos = gatos.exclude(id__in=Adotados.objects.values_list('gato_id', flat=True))

    # Filtro por nome
    nome = request.GET.get("nome")
    if nome:
        gatos = gatos.filter(nome__icontains=nome)

    # Filtro por sexo
    sexo = request.GET.get("sexo")
    if sexo in ["M", "F"]:
        gatos = gatos.filter(sexo=sexo)

    context = {
        "gatos": gatos,
    }
    return render(request, "gatos/dashboard_admin_adocoes.html", context)


# Função para excluir um gatinho - na tela dashboard_admin_adocoes
# Juntamente com a Pop-up de confirmação de exclusão
@require_POST
def excluir_gato_ajax(request, gato_id):
    try:
        gato = Gato.objects.get(id=gato_id)
        gato.delete()  
        return JsonResponse({"status": "ok", "mensagem": f"Gato {gato.nome} excluído com sucesso!"})
    except Gato.DoesNotExist:
        return JsonResponse({"status": "erro", "mensagem": "Gato não encontrado."}, status=404)
    
    
# ---------------------------------------------------------------------------------------- Da tela dashboard_admin_lar_temporario

# View que vai mandar as informações para os cards e tambem para o filtro
def dashboard_admin_lar_temporario(request):

    # Filtra apenas os gatos que precisam de lar temporário
    gatos = Gato.objects.filter(lar_temporario=True)

    # Excluir gatos que já foram adotados
    gatos = gatos.exclude(id__in=Adotados.objects.values_list('gato_id', flat=True))

    # Filtro por nome
    nome = request.GET.get("nome")
    if nome:
        gatos = gatos.filter(nome__icontains=nome)

    # Filtro por sexo
    sexo = request.GET.get("sexo")
    if sexo in ["M", "F"]:
        gatos = gatos.filter(sexo=sexo)

    # Pega os IDs dos gatos que estão em Lar Temporário atualmente
    gatos_em_lar_ids = LarTemporarioAtual.objects.values_list("gato_id", flat=True)

    # Marca cada gato se ele está ou não em lar temporário
    for gato in gatos:
        gato.em_lar = gato.id in gatos_em_lar_ids

    context = {
        "gatos": gatos,
    }

    return render(request, "gatos/dashboard_admin_lar_temporario.html", context)


logger = logging.getLogger(__name__)

class GatoCreateView(CreateView):
    model = Gato
    form_class = GatoForm
    template_name = 'gatos/adicionar_gato_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = self.request.POST or None
        context['gato_form'] = GatoForm(data, self.request.FILES or None)
        context['cuidado_form'] = CuidadoForm(data)
        context['temperamento_form'] = TemperamentoForm(data)
        context['moradia_form'] = MoradiaForm(data)
        context['sociavel_form'] = SociavelForm(data)
        return context

    def _save_related(self, form, gato):
        """
        Salva um formulário relacionado (Cuidado, Temperamento, etc.)
        tentando associar ao gato se existir campo 'gato' ou relação inversa.
        """
        instance = form.save(commit=False)
        if 'gato' in [f.name for f in form._meta.model._meta.get_fields()]:
            instance.gato = gato
        instance.save()

        # Checa se Gato possui campo que referencia o model
        for f in Gato._meta.get_fields():
            remote = getattr(f, 'remote_field', None)
            if remote and getattr(remote, 'model', None) == form._meta.model:
                setattr(gato, f.name, instance)
                gato.save()
                break

        return instance

    def post(self, request, *args, **kwargs):
        gato_form = GatoForm(request.POST, request.FILES)
        cuidado_form = CuidadoForm(request.POST)
        temperamento_form = TemperamentoForm(request.POST)
        moradia_form = MoradiaForm(request.POST)
        sociavel_form = SociavelForm(request.POST)

        if all(f.is_valid() for f in [gato_form, cuidado_form, temperamento_form, moradia_form, sociavel_form]):
            gato = gato_form.save()
            self._save_related(cuidado_form, gato)
            self._save_related(temperamento_form, gato)
            self._save_related(moradia_form, gato)
            self._save_related(sociavel_form, gato)

            messages.success(request, "Gato e formulários relacionados salvos com sucesso.")
            return redirect(self.get_success_url())
        
        # Renderiza com erros
        context = self.get_context_data()
        context['gato_form'] = gato_form
        context['cuidado_form'] = cuidado_form
        context['temperamento_form'] = temperamento_form
        context['moradia_form'] = moradia_form
        context['sociavel_form'] = sociavel_form
        return render(request, self.template_name, context)
# ---------------------------------------------------------------------------------------- Da tela dashboard_admin_adotados

# View que vai mandar as informações para os cards e tambem para o filtro
def dashboard_admin_adotados(request):
    # Pega todos os registros de adoção
    adotados = Adotados.objects.all()

    # Filtro por nome - nome do gato ou da pessoa
    nome = request.GET.get("nome")
    if nome:
        adotados = adotados.filter(
            Q(gato__nome__icontains=nome) |
            Q(adocao__nome__icontains=nome)
        )

    # Pega só o primeiro nome do adotante
    for adotado in adotados:
        adotado.adotante_primeiro_nome = adotado.adocao.nome.split()[0] if adotado.adocao.nome else ''

    context = {
        "adotados": adotados,
    }
    return render(request, "gatos/dashboard_admin_adotados.html", context)

# Função para excluir um registro de adoção - na tela dashboard_admin_adotaos
# Juntamente com a Pop-up de confirmação de exclusão
@require_POST
def excluir_adotado_ajax(request, adotado_id):
    try:
        adotado = Adotados.objects.get(id=adotado_id)
        adotado.delete()  
        return JsonResponse({"status": "ok", "mensagem": f"Gato {adotado.gato.nome} excluído com sucesso!"})
    except Adotados.DoesNotExist:
        return JsonResponse({"status": "erro", "mensagem": "Registro não encontrado."}, status=404)