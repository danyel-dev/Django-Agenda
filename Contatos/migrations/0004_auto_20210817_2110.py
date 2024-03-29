# Generated by Django 3.2.6 on 2021-08-18 00:10

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Contatos', '0003_contato_descricao_contato'),
    ]

    operations = [
        migrations.AddField(
            model_name='contato',
            name='categoria_contato',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Contatos.categoria'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contato',
            name='data_criacao_contato',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Data de criação'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contato',
            name='email_contato',
            field=models.CharField(blank=True, max_length=255, verbose_name='E-mail'),
        ),
        migrations.AddField(
            model_name='contato',
            name='nome_contato',
            field=models.CharField(default=1, max_length=255, verbose_name='Nome'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contato',
            name='sobrenome_contato',
            field=models.CharField(blank=True, max_length=255, verbose_name='Sobrenome'),
        ),
    ]
