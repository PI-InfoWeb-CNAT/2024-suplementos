# Generated by Django 5.1 on 2024-11-14 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0022_notificacao'),
    ]

    operations = [
        migrations.AddField(
            model_name='notificacao',
            name='titulo',
            field=models.CharField(default='Sem título', max_length=100),
            preserve_default=False,
        ),
    ]