from audioop import reverse

from django.core.validators import MaxValueValidator
from django.db import models


class Type_of_food(models.Model):
    type = models.CharField(max_length=100)
    def __str__(self):
        return self.type
    class Meta:
        verbose_name = 'Категории еды'
        verbose_name_plural = 'Категории еды'


class Food(models.Model):
    name_of_product = models.CharField(max_length=255)
    kkal = models.IntegerField(validators=[MaxValueValidator(2500)])
    proteins = models.FloatField(max_length=6)
    fats = models.FloatField(max_length=6)
    carbohydrates = models.FloatField(max_length=6)
    type_of_food = models.ForeignKey(Type_of_food, on_delete=models.PROTECT)

    def __str__(self):
        return self.name_of_product

    class Meta:
        verbose_name = 'Еда'
        verbose_name_plural = 'Еда'
