# Generated by Django 3.1.7 on 2021-02-26 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appva', '0006_merge_20210203_1544'),
    ]

    operations = [
        migrations.AddField(
            model_name='cci',
            name='desc_cnae',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
