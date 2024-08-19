# Generated by Django 5.1 on 2024-08-17 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='CEP',
            field=models.CharField(default='None', max_length=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='CPF',
            field=models.CharField(default='None', max_length=11),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='Endereco',
            field=models.CharField(default='None', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='Estado',
            field=models.CharField(default='None', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='Telefone_celular',
            field=models.CharField(default='None', max_length=11),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='Telefone_fixo',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='cliente',
            name='email',
            field=models.CharField(default='None', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='senha',
            field=models.CharField(default='None', max_length=100),
            preserve_default=False,
        ),
    ]