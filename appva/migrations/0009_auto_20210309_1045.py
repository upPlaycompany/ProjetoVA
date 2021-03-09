# Generated by Django 3.1.7 on 2021-03-09 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appva', '0008_cnae_arbitramento'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cfop',
            old_name='portaria',
            new_name='aplicacao',
        ),
        migrations.RenameField(
            model_name='cfop',
            old_name='status_cfop',
            new_name='codigo',
        ),
        migrations.RenameField(
            model_name='cfop',
            old_name='tipo_cfop',
            new_name='descricao',
        ),
        migrations.RemoveField(
            model_name='cfop',
            name='cfop',
        ),
        migrations.AddField(
            model_name='cfop',
            name='fim_vigencia',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='cfop',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cfop',
            name='inicio_vigencia',
            field=models.CharField(max_length=255, null=True),
        ),
    ]