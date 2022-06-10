"""Declare new app"""

from django.apps import AppConfig


class ArticlesConfig(AppConfig):
    """Config for app"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'articles'
