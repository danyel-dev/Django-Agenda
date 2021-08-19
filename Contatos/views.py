from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse

from .models import Contato


def home(request):
    contatos = Contato.objects.all()
    return render(request, 'Contatos/home.html', {'contatos': contatos})


def detalhes_contato(request, id_contato):
    contato = Contato.objects.get(id=id_contato)
    return render(request, 'Contatos/detalhes_contato.html', {'contato': contato})
