# Generated by Django 4.1.5 on 2023-01-15 16:44

import advertisements.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0009_alter_advertisement_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='is_published',
            field=models.BooleanField(validators=[advertisements.validators.check_ad_is_published]),
        ),
    ]
