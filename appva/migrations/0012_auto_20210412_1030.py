# Generated by Django 3.1.7 on 2021-04-12 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appva', '0011_auto_20210316_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='cfop',
            name='portaria',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='cfop',
            name='valido',
            field=models.CharField(max_length=3, null=True),
        ),
    ]
