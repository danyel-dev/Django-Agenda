from django.shortcuts import render
from django.http import HttpResponse

from .models import Contato


def home(request):
    contatos = Contato.objects.all()
    return render(request, 'agenda/home.html', {'contatos': contatos})
