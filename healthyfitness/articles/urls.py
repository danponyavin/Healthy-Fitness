from django.urls import path
from . import views

urlpatterns = [
    path('articles', views.allArticles, name='articles'),
    path('articles/health', views.healthArticles, name='articles_health'),
    # path('articles/health/<slug:art_slug>/', views.showArticle, name='oneArticle'),
    path('articles/devices', views.devicesArticles, name='articles_devices'),
    # path('articles/devices/<slug:art_slug>/', views.showArticle, name='oneArticle'),
    path('articles/food', views.foodArticles, name='articles_food'),
    # path('articles/food/<slug:art_slug>/', views.showArticle, name='oneArticle'),
    path('articles/sport', views.sportArticles, name='articles_sport'),
    # path('articles/sport/<slug:art_slug>/', views.showArticle, name='oneArticle'),
]