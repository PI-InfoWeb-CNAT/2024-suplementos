# Generated by Django 5.1 on 2024-09-26 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0011_rename_cpf_cliente_cpf_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='Dt_nasc',
        ),
    ]