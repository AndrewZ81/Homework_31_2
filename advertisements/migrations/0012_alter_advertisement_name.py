# Generated by Django 4.1.5 on 2023-01-15 19:18

import advertisements.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0011_alter_advertisement_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='name',
            field=models.CharField(max_length=200, validators=[advertisements.validators.check_ad_name_length]),
        ),
    ]
