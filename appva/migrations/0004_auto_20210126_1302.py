# Generated by Django 3.1.3 on 2021-01-26 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appva', '0003_auto_20210109_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acypr555',
            name='entradas',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='acypr555',
            name='ipi_entradas',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='acypr555',
            name='ipi_saidas',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='acypr555',
            name='saidas',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='acypr555',
            name='st_entradas',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='acypr555',
            name='st_saidas',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='acypr555',
            name='vr_adicionado',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='acypr557',
            name='entradas',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='acypr557',
            name='ipi_entradas',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='acypr557',
            name='ipi_saidas',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='acypr557',
            name='saidas',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='acypr557',
            name='st_entradas',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='acypr557',
            name='st_saidas',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='acypr557',
            name='vr_adicionado',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='acypr600',
            name='credito_ex_off',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='acypr600',
            name='debito_ex_off',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='acypr600',
            name='total',
            field=models.FloatField(null=True),
        ),
    ]
