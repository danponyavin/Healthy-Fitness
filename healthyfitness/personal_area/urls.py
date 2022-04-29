from django.urls import path
from . import views

urlpatterns = [
    path('personal_area', views.PersonalArea, name='personalArea'),
    ]