from django.contrib import admin
from .models import Type_of_food
from .models import Food


class Type_of_foodAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'photo')
    list_display_links = ('id', 'type')
    search_fields = ('type',)
    prepopulated_fields = {"slag": ("type",)}


class FoodAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_of_product', 'kkal', 'proteins', 'fats', 'carbohydrates')
    list_display_links = ('id', 'name_of_product')
    search_fields = ('name_of_product',)
    prepopulated_fields = {"slag": ("name_of_product",)}


admin.site.register(Type_of_food, Type_of_foodAdmin)
admin.site.register(Food, FoodAdmin)


