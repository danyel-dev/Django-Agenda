from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .forms import ContatoForm


def login(request):
    if request.method != 'POST':
        return render(request, 'accounts/login.html')

    username = request.POST.get('username')
    password = request.POST.get('password')

    user = auth.authenticate(request, username=username, password=password)

    if not user:
        messages.error(request, 'Usuário ou senha inválidos.')
        return render(request, 'accounts/login.html')
    
    auth.login(request, user)
    messages.success(request, 'Você fez login com sucesso!')

    return redirect('/')


# def logout(request):
#     auth.logout(request)
#     return redirect('login')


def register(request):
    if request.method != 'POST':
        return render(request, 'accounts/register.html')
    
    name = request.POST.get('name')
    lastname = request.POST.get('lastname')
    email = request.POST.get('email')
    username = request.POST.get('username')
    password = request.POST.get('password')
    passwordRepeat = request.POST.get('passwordRepeat')

    if not name or not lastname or not email or not username or not password or not passwordRepeat:
        messages.error(request, 'Nenhum campo pode ficar em branco!')
        return render(request, 'accounts/register.html')

    try:
        validate_email(email)
    except:
        messages.error(request, 'Email inválido!')
        return render(request, 'accounts/register.html')

    if len(username) < 6:
        messages.error(request, 'O nome de usuário tem que ter no mínimo 6 caracteres!')
        return render(request, 'accounts/register.html')

    if len(password) < 6:
        messages.error(request, 'A senha tem que ter no mínimo 6 caracteres!')
        return render(request, 'accounts/register.html')

    if password != passwordRepeat:
        messages.error(request, 'As senhas não são iguais')
        return render(request, 'accounts/register.html')

    if User.objects.filter(username=username).exists():
        messages.error(request, 'Esse usuário já existe')
        return render(request, 'accounts/register.html')

    if User.objects.filter(email=email).exists():
        messages.error(request, 'Esse usuário já existe')
        return render(request, 'accounts/register.html')

    user = User.objects.create_user(username=username, email=email, password=password, first_name=name, last_name=lastname)
    
    messages.success(request, 'Usuário registrado com sucesso!')
    
    user.save()
    return redirect('login')


@login_required(redirect_field_name='login')
def dashboard(request):
    if request.method != 'POST':    
        form = ContatoForm()
        return render(request, 'accounts/dashboard.html', {'form': form})

    form = ContatoForm(request.POST, request.FILES)

    if not form.is_valid():
        messages.error(request, 'Erro ao enviar o formulário')
        form = ContatoForm(request.POST)
        return render(request, 'accounts/dashboard.html', {'form': form})

    Contato = form.save(commit=False)
    Contato.user = request.user
    Contato.save()

    messages.success(request, f'{request.POST.get("nome_contato")} agora está salvo na sua agenda!')

    return redirect('/')
