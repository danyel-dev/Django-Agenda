from django.db import models


class Categoria(models.Model):
    nome_categoria = models.CharField(max_length=225, verbose_name='Nome da categoria')


    def __str__(self):
        return self.nome_categoria


class Contato(models.Model):
    categoria_contato = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING, verbose_name='Categoria')

    nome_contato = models.CharField(max_length=100, verbose_name='Nome')
    
    sobrenome_contato = models.CharField(max_length=100, verbose_name='Sobrenome')
    
    telefone_contato = models.CharField(max_length=225, verbose_name='Telefone')
    
    email_contato = models.CharField(max_length=255, blank=True, verbose_name='E-mail')    
    
    data_criacao_contato = models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')

    descricao_contato = models.TextField(blank=True, verbose_name='Descrição')

    mostrar_contato = models.BooleanField(default=False)

    image_contact = models.ImageField(blank=True, upload_to='imagens/%Y/%m/%d')


    def __str__(self):
        return self.nome_contato
