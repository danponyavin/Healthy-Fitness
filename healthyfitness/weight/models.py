from django.core.validators import MaxValueValidator
from django.db import models


class Weight_trecker(models.Model):
    id_users = models.ForeignKey('calculator.Profile', on_delete=models.PROTECT)
    day_create = models.DateField(auto_now_add=True)
    weight = models.FloatField(null=True, validators=[MaxValueValidator(400)])

    def __str__(self):
        return str(self.weight)

    class Meta:
        verbose_name = 'Трекер веса'
        verbose_name_plural = 'Трекер веса'
        ordering = ['day_create']
