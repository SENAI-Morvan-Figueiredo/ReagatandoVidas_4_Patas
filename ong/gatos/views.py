import logging
from django.views.generic import CreateView
from django.shortcuts import render , redirect , get_list_or_404
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
    success_url = reverse_lazy('dashboard_admin_adocoes')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = self.request.POST or None
        files = self.request.FILES or None

        context['gato_form'] = context.get('form')  # principal
        context['cuidado_form'] = kwargs.get('cuidado_form') or CuidadoForm(data, prefix='cuidado')
        context['temperamento_form'] = kwargs.get('temperamento_form') or TemperamentoForm(data, prefix='temperamento')
        context['moradia_form'] = kwargs.get('moradia_form') or MoradiaForm(data, prefix='moradia')
        context['sociavel_form'] = kwargs.get('sociavel_form') or SociavelForm(data, prefix='sociavel')
        return context

    def post(self, request, *args, **kwargs):
        # todos os forms de uma vez
        form = self.get_form()
        cuidado_form = CuidadoForm(request.POST, prefix='cuidado')
        temperamento_form = TemperamentoForm(request.POST, prefix='temperamento')
        moradia_form = MoradiaForm(request.POST, prefix='moradia')
        sociavel_form = SociavelForm(request.POST, prefix='sociavel')


        if all([
            form.is_valid(),
            cuidado_form.is_valid(),
            temperamento_form.is_valid(),
            moradia_form.is_valid(),
            sociavel_form.is_valid()
        ]):
            
            cuidado = cuidado_form.save()
            temperamento = temperamento_form.save()
            moradia = moradia_form.save()
            sociavel = sociavel_form.save()

            gato = form.save(commit=False)
            gato.cuidado = cuidado
            gato.temperamento = temperamento
            gato.moradia = moradia
            gato.sociavel = sociavel
            gato.save()
    
            messages.success(request, "Gato e informações relacionadas salvos com sucesso!")
            return redirect(self.success_url)
        else:

            self.object = None  # Necessário para renderizar o template corretamente
            context = self.get_context_data(
                form=form,
                cuidado_form=cuidado_form,
                temperamento_form=temperamento_form,
                moradia_form=moradia_form,
                sociavel_form=sociavel_form
            )
            print("❌ Formulário inválido:", form.errors)
            for f in [cuidado_form, temperamento_form, moradia_form, sociavel_form]:
                if f.errors:
                     print(f"⚠️ Erros em {f.__class__.__name__}:", f.errors)
            return self.render_to_response(context)
      


    # def form_invalid(self, form, *related_forms):
    #     """Exibe erros de validação de todos os formulários."""
    #     if not related_forms:
    #         cuidado_form = CuidadoForm(self.request.POST or None)
    #         temperamento_form = TemperamentoForm(self.request.POST or None)
    #         moradia_form = MoradiaForm(self.request.POST or None)
    #         sociavel_form = SociavelForm(self.request.POST or None)
    #     else:
    #         cuidado_form, temperamento_form, moradia_form, sociavel_form = related_forms

    #     context = self.get_context_data(
    #         cuidado_form=cuidado_form,
    #         temperamento_form=temperamento_form,
    #         moradia_form=moradia_form,
    #         sociavel_form=sociavel_form
    #     )
    #     context['form'] = form

    #     if form.errors:
    #         print("❌ Erros em GatoForm:", form.errors)
    #         messages.error(self.request, f"Erros em GatoForm: {form.errors}")

    #     for related in related_forms or []:
    #         if related.errors:
    #             print(f"⚠️ Erros em {related.__class__.__name__}: {related.errors}")
    #             messages.error(self.request, f"Erros em {related.__class__.__name__}: {related.errors}")

    #     return self.render_to_response(context)

# ---------------------------------------------------------------------------------------- Da tela dashboard_admin_adotados

# View que vai mandar as informações para os cards e tambem para o filtro
def dashboard_admin_adotados(request):
    # Pega todos os registros de adoção com os relacionamentos otimizados
    adotados = Adotados.objects.select_related('adocao', 'gato')

    # Filtro por nome - nome do gato ou da pessoa
    nome = request.GET.get("nome")
    if nome:
        adotados = adotados.filter(
            Q(gato__nome__icontains=nome) |
            Q(adocao__nome__icontains=nome)
        )

    # Pega dados do adotante para facilitar no template
    for adotado in adotados:
        adotado.adotante_primeiro_nome = adotado.adocao.nome.split()[0] if adotado.adocao.nome else ''
        adotado.adotante_nome = adotado.adocao.nome
        adotado.adotante_email = adotado.adocao.email
        adotado.adotante_telefone = adotado.adocao.numero_contato

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