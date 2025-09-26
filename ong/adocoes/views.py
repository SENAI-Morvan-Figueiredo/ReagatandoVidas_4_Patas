from django.shortcuts import render , redirect
from .models import Adocao

# Create your views here.

from .forms import AdocaoForm

def nova_adocao(request):
    if request.method == 'POST':
        form = AdocaoForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('lista_adocoes')
    else:
        form = AdocaoForm()

    return render(request, 'adocoes/form_adocao.html', {'form': form})

def lista_adocoes(request):
    adocoes = Adocao.objects.all()  # SELECT * FROM adocoes_adocao;
    return render(request, 'adocoes/lista_adocoes.html', {'adocoes': adocoes})