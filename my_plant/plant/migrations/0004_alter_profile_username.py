# Generated by Django 4.1.4 on 2022-12-21 08:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plant', '0003_alter_profile_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(2)]),
        ),
    ]