# Generated by Django 5.1 on 2024-10-19 01:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0016_remove_cliente_email_alter_cliente_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='Telefone_fixo',
        ),
    ]