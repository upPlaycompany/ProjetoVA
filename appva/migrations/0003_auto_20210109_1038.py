# Generated by Django 3.1.3 on 2021-01-09 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appva', '0002_auto_20201230_1113'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fpm',
            old_name='municipio',
            new_name='ano',
        ),
        migrations.AddField(
            model_name='fpm',
            name='abril',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='fpm',
            name='agosto',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='fpm',
            name='dezembro',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='fpm',
            name='fevereiro',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='fpm',
            name='janeiro',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='fpm',
            name='julho',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='fpm',
            name='junho',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='fpm',
            name='maio',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='fpm',
            name='marco',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='fpm',
            name='novembro',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='fpm',
            name='outubro',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='fpm',
            name='setembro',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='fpm',
            name='variacao',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='acypr535',
            name='area',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='acypr535',
            name='coef_soc',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='acypr535',
            name='ind_final',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='acypr535',
            name='iva_75',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='acypr535',
            name='iva_ant',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='acypr535',
            name='iva_atual',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='acypr535',
            name='iva_med',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='acypr535',
            name='populacao',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='acypr535',
            name='trib_propr',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='acypr535',
            name='ucti',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='acypr540',
            name='ipm_ano_base',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='acypr540',
            name='ipm_ano_exercicio',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='acypr540',
            name='porcentagem',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='acypr556',
            name='area',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='acypr556',
            name='populacao',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='acypr556',
            name='receita_propria',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='acypr556',
            name='vr_adic_ano_base',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='acypr556',
            name='vr_adic_ano_exercicio',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='fpm',
            name='total',
            field=models.FloatField(null=True),
        ),
    ]
