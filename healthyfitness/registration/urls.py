from django.urls import path
from . import views
from .views import RegisterUser

urlpatterns = [
    path('login/', views.login, name='login'),
    path('registration/', RegisterUser.as_view(), name='registration_field'),

]

