# Generated by Django 3.2.4 on 2021-06-29 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stnk', '0003_auto_20210628_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='masa_aktif',
            field=models.DateTimeField(),
        ),
    ]