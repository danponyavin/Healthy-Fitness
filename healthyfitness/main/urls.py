from django.urls import path
from . import views


urlpatterns = [
    path('', views.main_page, name='home'),
    path('calculator', views.calculator, name='calculator'),
    path('blog', views.blog, name='blog'),
    path('personal_area', views.personal_area, name='personal_area'),
]
