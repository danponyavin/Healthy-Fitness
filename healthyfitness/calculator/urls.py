from django.urls import path
from django.conf.urls.static import static

from healthyfitness import settings
from . import views


urlpatterns = [
    path('calculator', views.calculator, name='calculator'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
