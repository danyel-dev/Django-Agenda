from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('<int:id_contato>', views.detalhes_contato, name='detalhes_contato'),
]
