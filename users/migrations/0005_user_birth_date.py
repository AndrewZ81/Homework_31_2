# Generated by Django 4.1.5 on 2023-01-16 10:47

from django.db import migrations, models
import users.validators


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='birth_date',
            field=models.DateField(null=True, validators=[users.validators.check_user_age]),
        ),
    ]