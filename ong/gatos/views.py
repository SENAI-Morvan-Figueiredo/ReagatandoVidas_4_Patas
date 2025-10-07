import logging
from django.views.generic import CreateView
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from gatos.models import Gato 
from lares_temporarios.models import LarTemporarioAtual
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from .forms import GatoForm

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

    def get_initial(self):
        initial = super().get_initial()
        gato_id = self.request.GET.get('gato')
        if gato_id:
            try:
                gato = get_object_or_404(Gato, pk=gato_id)
                initial['gato'] = gato
            except Exception:
                pass
        return initial

    def form_valid(self, form):
        gato = form.cleaned_data.get('gato')
        if not gato:
            gato_id = self.request.GET.get('gato')
            if gato_id:
                form.instance.gato = get_object_or_404(Gato, pk=gato_id)
        response = super().form_valid(form)
        messages.success(self.request, "Solicitação de adoção enviada com sucesso.")
        return response