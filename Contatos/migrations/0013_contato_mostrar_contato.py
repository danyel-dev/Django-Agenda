# Generated by Django 3.2.6 on 2021-08-20 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Contatos', '0012_auto_20210819_1220'),
    ]

    operations = [
        migrations.AddField(
            model_name='contato',
            name='mostrar_contato',
            field=models.BooleanField(default=True),
        ),
    ]
