import logging
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404 , render, redirect
from django.contrib import messages
from django.core.exceptions import FieldError
from .models import Adocao , Adotados
from gatos.models import Gato
from .forms import AdocaoForm
from django.utils.timezone import now

logger = logging.getLogger(__name__)

class GatoListView(ListView):
    model = Gato
    template_name = 'adocoes/adocao_list.html'
    context_object_name = 'gatos'
    paginate_by = 12

    def get_queryset(self):
        try:
            qs = Gato.objects.filter(adotados__isnull=True)
            try:
                qs = qs.order_by('-created_at')
            except FieldError:
                qs = qs.order_by('-id')
            q = self.request.GET.get('q')
            sexo_filter = self.request.GET.get('sexo')

            if q:
                qs = qs.filter(nome__icontains=q)

            if sexo_filter == 'fêmea':
                qs = qs.filter(sexo__lte=1)
            elif sexo_filter == 'macho':
                qs = qs.filter(sexo__gt=1)
            return qs

        except Exception as e:
            logger.exception("Erro em GatoListView.get_queryset: %s", e)
            return Gato.objects.none()


class GatoDetailView(DetailView):
    model = Gato
    template_name = 'adocoes/adocao_detail.html'
    context_object_name = 'gato'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        # Outros gatos para exibir — exclui o atual
        ctx['other_gatos'] = Gato.objects.filter(adotados__isnull=True).exclude(pk=self.object.pk)[:4]
        return ctx


def adocao_sucess(request):
    return render(request, 'adocoes/adocao_sucess.html')

def formulario_adocao(request):
    gato_id = request.GET.get('gato')
    gato = None

    if gato_id:
        gato = get_object_or_404(Gato, id=gato_id)

    if request.method == 'POST':
        form = AdocaoForm(request.POST)
        if form.is_valid():
            adocao = form.save()

            gato = adocao.gato

            gato.adotado = True
            gato.save()

            Adotados.objects.create(
                imagem=gato.imagem,
                gato=gato,
                adocao=adocao,
                data_inicio=now().date(),
            )

            # Redireciona para a tela de sucesso
            return redirect('adocoes:adocao_sucess')
    else:
        form = AdocaoForm()

    return render(request, 'adocoes/adocao_form.html', {'form': form})

