from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('registration.urls')),
    path('', include('main.urls')),
    path('', include('articles.urls')),
    path('', include('calculator.urls')),
    path('', include('food_diary.urls')),

]
