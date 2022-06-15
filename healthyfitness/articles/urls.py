from django.conf.urls.static import static
from django.urls import path

from healthyfitness import settings
from . import views

urlpatterns = [
    path('articles', views.all_articles, name='articles'),
    path('articles/health', views.health_articles, name='articles_health'),
    path('articles/devices', views.devices_articles, name='articles_devices'),
    path('articles/food', views.food_articles, name='articles_food'),
    path('articles/sport', views.sport_articles, name='articles_sport'),
    path('articles/<slug:art_slug>', views.show_certain_article, name='certainArticle'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
