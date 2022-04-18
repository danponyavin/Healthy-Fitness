# Generated by Django 4.0.3 on 2022-04-13 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about_user',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='about_user',
            name='growth',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='about_user',
            name='needed_carbohydrates',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='about_user',
            name='needed_fats',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='about_user',
            name='needed_kkal',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='about_user',
            name='needed_proteins',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='about_user',
            name='weight',
            field=models.FloatField(null=True),
        ),
    ]
