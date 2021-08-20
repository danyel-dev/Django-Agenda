from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('search-contact/', views.search_contact, name='search_contact'),
    path('<int:id_contato>/', views.detalhes_contato, name='detalhes_contato'),
]
