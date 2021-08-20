from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.db.models.functions import Concat

from .models import Contato


def home(request):
    contatos = Contato.objects.order_by('-id').filter(mostrar_contato=True)

    paginator = Paginator(contatos, 5)
    page = request.GET.get('page')
    contatos = paginator.get_page(page)

    return render(request, 'Contatos/home.html', {'contatos': contatos})


def search_contact(request):
    term = request.GET.get('term')
    
    campos = Concat("nome_contato", Value(" "), "sobrenome_contato")

    contatos = Contato.objects.annotate(
        nome_completo = campos
    ).filter(
        Q(nome_completo__icontains = term) | Q(telefone_contato__icontains = term),
        mostrar_contato = True
    )

    paginator = Paginator(contatos, 5)
    page = request.GET.get('page')
    contatos = paginator.get_page(page)

    return render(request, 'Contatos/home.html', {'contatos': contatos})


def detalhes_contato(request, id_contato):
    contato = get_object_or_404(Contato, id=id_contato)

    if not contato.mostrar_contato:
        raise Http404()

    return render(request, 'Contatos/detalhes_contato.html', {'contato': contato})
