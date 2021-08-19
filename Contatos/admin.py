from django.contrib import admin

from .models import Categoria, Contato


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_categoria',)
    list_display_links = ('id', 'nome_categoria',)


class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_contato', 'telefone_contato', 'categoria_contato', 'data_criacao_contato')
    list_display_links = ('id', 'nome_contato', 'telefone_contato',)
    list_editable = ('categoria_contato',)


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Contato, ContatoAdmin)
