# Generated by Django 4.0.3 on 2022-04-18 19:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_diary', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='kkal',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(999)]),
        ),
    ]
