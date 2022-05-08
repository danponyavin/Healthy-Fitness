from django.urls import path
from . import views

urlpatterns = [
    path('personal_area', views.PersonalArea, name='personalArea'),
    path('change_information', views.image_upload_view, name='change_information'),
]
    