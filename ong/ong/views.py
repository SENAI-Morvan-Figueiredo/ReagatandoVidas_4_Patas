from django.shortcuts import render

def doacoes(request):
    return render(request, 'ong/doacao.html')