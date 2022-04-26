from django.conf.urls.static import static
from django.urls import path
from healthyfitness import settings
from . import views

urlpatterns = [
    path('personal_area/food_diary', views.UserFood, name='food_diary'),
    path('personal_area/product_selection', views.ProductSelection, name='product_selection'),
    path('personal_area/product_selection/bakery', views.Bakery, name='bakery'),
    path('personal_area/product_selection/cereals', views.Cereals, name='cereals'),
    path('personal_area/product_selection/meat', views.Meat, name='meat'),
    path('personal_area/product_selection/vegFruit', views.VegFruit, name='vegFruit'),
    path('personal_area/product_selection/seafood', views.Seafood, name='seafood'),
    path('personal_area/product_selection/cookedMeals', views.CookedMeals, name='cookedMeals'),
    path('personal_area/product_selection/milk', views.Milk, name='milk'),
    path('personal_area/product_selection/sweets', views.Sweets, name='sweets'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
