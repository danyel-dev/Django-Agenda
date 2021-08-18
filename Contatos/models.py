from django.db import models


class Categoria(models.Model):
    nome_categoria = models.CharField(max_length=255, verbose_name='Nome da categoria')


    def __str__(self):
        return self.nome_categoria


class Contato(models.Model):
    categoria_contato = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='Categoria')

    nome_contato = models.CharField(max_length=255, verbose_name='Nome')
    
    sobrenome_contato = models.CharField(max_length=255, blank=True, verbose_name='Sobrenome')
    
    telefone_contato = models.CharField(max_length=12, verbose_name='Telefone')
    
    email_contato = models.CharField(max_length=255, blank=True, verbose_name='E-mail')    
    
    data_criacao_contato = models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')

    descricao_contato = models.TextField(blank=True, verbose_name='Descrição')


    def __str__(self):
        return self.nome_contato
