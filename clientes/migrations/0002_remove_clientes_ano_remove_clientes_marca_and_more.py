# Generated by Django 4.2.2 on 2023-06-17 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientes',
            name='ano',
        ),
        migrations.RemoveField(
            model_name='clientes',
            name='marca',
        ),
        migrations.RemoveField(
            model_name='clientes',
            name='modelo',
        ),
        migrations.AddField(
            model_name='clientes',
            name='carro',
            field=models.ManyToManyField(blank=True, related_name='carro_cliente', to='clientes.carro'),
        ),
    ]
