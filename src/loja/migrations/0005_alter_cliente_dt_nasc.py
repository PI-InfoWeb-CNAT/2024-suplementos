# Generated by Django 5.1 on 2024-08-12 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0004_alter_cliente_dt_nasc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='Dt_nasc',
            field=models.DateField(default='2000-01-01'),
        ),
    ]