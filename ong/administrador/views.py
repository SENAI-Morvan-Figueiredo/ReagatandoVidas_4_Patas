from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Adminstrador

def login_view(request):
    # A mensagem de erro só pode ser criada dentro deste bloco POST
    if request.method == "POST":
        email = request.POST.get("email")
        senha = request.POST.get("senha")

        try:
            admin = Adminstrador.objects.get(email=email, senha=senha)
            # Login bem-sucedido, limpa a sessão e cria uma nova
            request.session.flush() 
            request.session["admin_id"] = admin.id
            request.session["admin_email"] = admin.email
            return redirect("dashboard")
        except Adminstrador.DoesNotExist:
            # Apenas aqui a mensagem de erro é criada
            messages.error(request, "Email ou senha inválidos.")
            # Importante: redirecionar para a própria página de login
            # Isso garante que a página seja recarregada com o método GET
            # e o contexto de mensagens seja exibido corretamente.
            return redirect("login") 

    # Se o método for GET (primeiro acesso à página), nenhuma mensagem é criada.
    return render(request, "administrador/login.html")

def logout_view(request):
    request.session.flush()  # remove todos os dados da sessão
    return redirect("login")

def dashboard_view(request):
    if not request.session.get("admin_id"):
        return redirect("login")  # se não estiver logado, volta para o login
    return render(request, "administrador/dashboard.html")
