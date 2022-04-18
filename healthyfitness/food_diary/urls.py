from django.urls import path
from . import views

urlpatterns = [
    path('personal_area/food_diary', views.UserFood, name='food_diary'),
    path('personal_area/product_selection', views.ProductSelection, name='product_selection'),
]
