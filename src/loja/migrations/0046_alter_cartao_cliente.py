# Generated by Django 5.1 on 2025-01-21 01:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0045_alter_endereco_cliente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartao',
            name='cliente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cartoes', to='loja.cliente'),
        ),
    ]
