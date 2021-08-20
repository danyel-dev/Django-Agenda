from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.core.paginator import Paginator
from .models import Contato


def home(request):
    contatos = Contato.objects.order_by('-id').filter(mostrar_contato=True)
    
    paginator = Paginator(contatos, 5)
    page = request.GET.get('page')
    contatos = paginator.get_page(page)

    return render(request, 'Contatos/home.html', {'contatos': contatos})

    
def detalhes_contato(request, id_contato):
    contato = get_object_or_404(Contato, id=id_contato)

    if not contato.mostrar_contato:
        raise Http404()

    return render(request, 'Contatos/detalhes_contato.html', {'contato': contato})
