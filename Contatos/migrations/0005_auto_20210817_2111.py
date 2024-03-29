# Generated by Django 3.2.6 on 2021-08-18 00:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Contatos', '0004_auto_20210817_2110'),
    ]

    operations = [
        migrations.AddField(
            model_name='contato',
            name='telefone_contato',
            field=models.CharField(default=1, max_length=12, verbose_name='Telefone'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contato',
            name='categoria_contato',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='Contatos.categoria'),
        ),
    ]
