import logging
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.core.exceptions import FieldError
from .models import Adocao
from gatos.models import Gato
from .forms import AdocaoForm

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


class AdocaoCreateView(CreateView):
    model = Adocao
    form_class = AdocaoForm
    template_name = 'adocoes/adocao_form.html'

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

    def get_success_url(self):
        return reverse_lazy('adocoes:adocao_success')


class AdocaoSuccessView(TemplateView):
    template_name = 'adocoes/adocao_success.html'