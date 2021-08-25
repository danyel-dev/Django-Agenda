from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Contato


@login_required(redirect_field_name='login')
def home(request):
    contatos = Contato.objects.order_by('-id').filter(mostrar_contato=True, user=request.user)
  
    paginator = Paginator(contatos, 5)
    page = request.GET.get('page')
    contatos = paginator.get_page(page)

    return render(request, 'contatos/home.html', {'contatos': contatos})


def search_contact(request):
    term = request.GET.get('term')
    
    if not term or term is None:
        messages.add_message(request, messages.ERROR, 'Você deixou o campo em branco, nada encontrado!')

        return redirect('/')

    campos = Concat("nome_contato", Value(" "), "sobrenome_contato")

    contatos = Contato.objects.annotate(
        nome_completo = campos
    ).filter(
        Q(nome_completo__icontains = term) | Q(telefone_contato__icontains = term),
        mostrar_contato = True
    )

    if not contatos:
        messages.add_message(request, messages.ERROR, 'Nenhum contato encontrado!')

        return redirect('/')

    paginator = Paginator(contatos, 5)
    page = request.GET.get('page')
    contatos = paginator.get_page(page)

    return render(request, 'contatos/home.html', {'contatos': contatos})


@login_required(redirect_field_name='login')
def detalhes_contato(request, id_contato):
    contato = get_object_or_404(Contato, id=id_contato)

    if not contato.mostrar_contato:
        raise Http404()

    return render(request, 'contatos/detalhes_contato.html', {'contato': contato})
