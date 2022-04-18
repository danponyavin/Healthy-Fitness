from django.contrib import admin

from .models import About_user


class About_userAdmin(admin.ModelAdmin):
    list_display = ('user', 'age', 'weight', 'gender', 'growth', 'Activity_level', 'user_aim', 'needed_kkal', 'needed_proteins', 'needed_fats', 'needed_carbohydrates')
    prepopulated_fields = {"slag": ("user",)}


admin.site.register(About_user, About_userAdmin)
