import logging
from django.views.generic import CreateView
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from gatos.models import Gato, Cuidado
from lares_temporarios.models import LarTemporarioAtual
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from .forms import GatoForm, CuidadoForm

# ---------------------------------------------------------------------------------------- Da tela dashboard_admin_adocoes

# View que vai mandar as informações para os cards e tambem para o filtro
def dashboard_admin_adocoes(request):
    # Pega todos os gatos
    gatos = Gato.objects.all()

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
    """
    View para o dashboard de gatos que precisam ou estão em lar temporário.
    """

    # Filtra apenas os gatos que precisam de lar temporário
    gatos = Gato.objects.filter(lar_temporario=True)

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
        # se vier em GET com dados, preserve-os
        if self.request.POST:
            context['gato_form'] = GatoForm(self.request.POST, self.request.FILES)
            context['cuidado_form'] = CuidadoForm(self.request.POST)
        else:
            context['gato_form'] = GatoForm()
            context['cuidado_form'] = CuidadoForm()
        return context

    def post(self, request, *args, **kwargs):
        gato_form = GatoForm(request.POST, request.FILES)
        cuidado_form = CuidadoForm(request.POST)

        if gato_form.is_valid() and cuidado_form.is_valid():
            # Salva o gato primeiro
            gato = gato_form.save()

            # Salva o cuidado sem commitar ainda, pra ligar ao gato se necessário
            cuidado = cuidado_form.save(commit=False)

            # --- Tenta achar relacionamento automaticamente ---
            # 1) Se Cuidado tem campo 'gato', atribui
            cuidado_fields = [f.name for f in Cuidado._meta.get_fields()]
            if 'gato' in cuidado_fields:
                try:
                    cuidado.gato = gato
                    cuidado.save()
                except Exception as e:
                    logger.exception("Erro ao salvar Cuidado com FK 'gato': %s", e)
                    # tenta salvar sem ligação
                    cuidado.save()
            else:
                # 2) verifica se Gato tem algum campo que referencia Cuidado (OneToOneField / FK)
                campo_relacionado = None
                for f in Gato._meta.get_fields():
                    remote = getattr(f, 'remote_field', None)
                    if remote and getattr(remote, 'model', None) == Cuidado:
                        campo_relacionado = f.name
                        break

                if campo_relacionado:
                    # salva cuidado, depois associa no gato
                    cuidado.save()
                    try:
                        setattr(gato, campo_relacionado, cuidado)
                        gato.save()
                    except Exception as e:
                        logger.exception("Erro ao associar Cuidado ao Gato via campo '%s': %s", campo_relacionado, e)
                else:
                    # Caso nenhum relacionamento direto, apenas salva o cuidado normalmente
                    cuidado.save()

            messages.success(request, "Gato e cuidados veterinários salvos com sucesso.")
            return redirect(self.get_success_url())
        else:
            # se inválidos, renderiza o template com os forms e erros
            context = self.get_context_data()
            context['gato_form'] = gato_form
            context['cuidado_form'] = cuidado_form
            return render(request, self.template_name, context)