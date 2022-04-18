from django.conf.urls.static import static
from django.urls import path
from healthyfitness import settings
from . import views

urlpatterns = [
    path('personal_area/food_diary', views.UserFood, name='food_diary'),
    path('personal_area/product_selection', views.ProductSelection, name='product_selection'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
