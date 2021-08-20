from django.contrib import admin

from .models import Categoria, Contato


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_categoria',)
    list_display_links = ('id', 'nome_categoria',)


class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_contato', 'sobrenome_contato', 'telefone_contato', 'data_criacao_contato', 'categoria_contato', 'mostrar_contato')
    
    list_display_links = ('id', 'nome_contato', 'sobrenome_contato', 'telefone_contato')
    
    list_editable = ('categoria_contato', 'mostrar_contato',)
    
    list_per_page = 5
    
    list_filter = ('sobrenome_contato', 'categoria_contato')
    
    search_fields = ('nome_contato', 'telefone_contato')


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Contato, ContatoAdmin)
