# Generated by Django 3.2.6 on 2021-08-20 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Contatos', '0014_alter_contato_mostrar_contato'),
    ]

    operations = [
        migrations.AddField(
            model_name='contato',
            name='image_contact',
            field=models.ImageField(blank=True, upload_to='imagens/%Y/%m/%d'),
        ),
    ]