from django import forms
from django.db import models


class Calculator(models.Model):

    age = models.CharField('', max_length=3)
    weight = models.CharField('', max_length=5)
    growth = models.CharField('', max_length=3)
    select_gender = (
        (None, 'Укажите пол'),
        ('1', "Мужской"),
        ('2', "Женский")
    )
    gender = models.CharField(max_length=1, choices=select_gender, default=None)
    select_aim = (
        (None, 'Укажите цель'),
        ('1', "Похудение"),
        ('2', "Поддержание веса"),
        ('3', "Набор мышечной массы"),
    )
    user_aim = models.CharField(max_length=1, choices=select_aim)
    select_activity = (
        (None, 'Укажите активность'),
        ('1', "Отсутствие активности"),
        ('2', "Низкая активность"),
        ('3', "Средняя активность"),
        ('4', "Высокая активность"),
        ('5', "Экстремальная активность"),
    )
    user_activity = models.CharField(max_length=100, choices=select_activity)

