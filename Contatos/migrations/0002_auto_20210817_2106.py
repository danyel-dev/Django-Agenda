# Generated by Django 3.2.6 on 2021-08-18 00:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Contatos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contato',
            name='categoria_contato',
        ),
        migrations.RemoveField(
            model_name='contato',
            name='data_criacao_contato',
        ),
        migrations.RemoveField(
            model_name='contato',
            name='descricao_contato',
        ),
        migrations.RemoveField(
            model_name='contato',
            name='email_contato',
        ),
        migrations.RemoveField(
            model_name='contato',
            name='sobrenome_contato',
        ),
        migrations.RemoveField(
            model_name='contato',
            name='telefone_contato',
        ),
    ]