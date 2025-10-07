from django.shortcuts import render, redirect
from gatos.models import Gato 
from lares_temporarios.models import LarTemporarioAtual
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from .forms import GatoCompletoForm


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
    
def adicionar_gato(request):
    if request.method == 'POST':
        form = GatoCompletoForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            gato = form.save()
            messages.success(request, f'Gato "{gato.nome}" adicionado com sucesso!')
            return redirect('gatos:lista_gatos')  # Ajuste conforme sua URL
        else:
            messages.error(request, 'Erro ao salvar o gato. Verifique os dados.')
    else:
        form = GatoCompletoForm()
    
    return render(request, 'gatos/adicionar_gato.html', {'form': form})

def editar_gato(request, gato_id):
    from .models import Gato
    from django.get_object_or_404 import get_object_or_404
    
    gato = get_object_or_404(Gato, id=gato_id)
    
    if request.method == 'POST':
        form = GatoCompletoForm(data=request.POST, files=request.FILES, instance=gato)
        if form.is_valid():
            gato = form.save()
            messages.success(request, f'Gato "{gato.nome}" atualizado com sucesso!')
            return redirect('gatos:lista_gatos')  # Ajuste conforme sua URL
        else:
            messages.error(request, 'Erro ao atualizar o gato. Verifique os dados.')
    else:
        form = GatoCompletoForm(instance=gato)
    
    return render(request, 'gatos/adicionar_gato.html', {'form': form, 'gato': gato})
    
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

