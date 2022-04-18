# Generated by Django 4.0.3 on 2022-04-18 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calculator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.CharField(max_length=3, verbose_name='')),
                ('weight', models.CharField(max_length=5, verbose_name='')),
                ('growth', models.CharField(max_length=3, verbose_name='')),
                ('gender', models.CharField(choices=[(None, 'Укажите пол'), ('1', 'Мужской'), ('2', 'Женский')], default=None, max_length=1)),
                ('user_aim', models.CharField(choices=[(None, 'Укажите цель'), ('1', 'Похудение'), ('2', 'Поддержание веса'), ('3', 'Набор мышечной массы')], max_length=1)),
                ('user_activity', models.CharField(choices=[(None, 'Укажите активность'), ('1', 'Отсутствие активности'), ('2', 'Низкая активность'), ('3', 'Средняя активность'), ('4', 'Высокая активность'), ('5', 'Экстремальная активность')], max_length=100)),
            ],
        ),
    ]
