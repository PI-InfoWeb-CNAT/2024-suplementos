# Generated by Django 5.1 on 2024-12-05 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0036_rename_categoria_produto_categoria_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='CPF',
            new_name='cpf',
        ),
        migrations.RenameField(
            model_name='cliente',
            old_name='Nome',
            new_name='nome',
        ),
        migrations.RenameField(
            model_name='cliente',
            old_name='Telefone_celular',
            new_name='telefone_celular',
        ),
    ]
