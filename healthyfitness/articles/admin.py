"""Contains admin-panel classes"""

from django.contrib import admin
from .models import Category
from .models import Article


class CategoryAdmin(admin.ModelAdmin):
    """Admin for article categories"""
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slag": ("name",)}


class ArticleAdmin(admin.ModelAdmin):
    """Admin for articles"""
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_filter = ('time_create',)
    prepopulated_fields = {"slag": ("title",)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
