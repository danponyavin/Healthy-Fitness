"""Models for articles"""

from audioop import reverse
from django.db import models


class Category(models.Model):
    """Category model"""
    name = models.CharField(max_length=100)
    slag = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    class Meta:
        """Class for translate to russian"""
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'


class Article(models.Model):
    """Model for article"""
    title = models.CharField(max_length=255)
    slag = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Returns full url"""
        return reverse('post', kwargs={'post_slug': self.slag})

    class Meta:
        """Class for translate to russian"""
        verbose_name = 'Статьи'
        verbose_name_plural = 'Статьи'
