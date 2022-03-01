from django.urls import path
from . import views


urlpatterns = [
    path('', views.main_page, name='home'),
    path('articles', views.articles, name='articles'),
    path('calculator', views.calculator, name='calculator'),
    path('blog', views.blog, name='blog'),
    path('food_diary', views.food_diary, name='food_diary'),
    path('personal_area', views.personal_area, name='personal_area'),
    path('registration_field', views.registration_field, name='registration_field')
]