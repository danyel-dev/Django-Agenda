# Generated by Django 3.2.6 on 2021-08-20 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Contatos', '0013_contato_mostrar_contato'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='mostrar_contato',
            field=models.BooleanField(default=False),
        ),
    ]
