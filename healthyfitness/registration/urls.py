from django.urls import path
from . import views
from .views import RegisterUser, LoginUser, logout_user

urlpatterns = [
    path('login/', LoginUser.as_view(), name='login'),
    path('registration/', RegisterUser.as_view(), name='registration_field'),
    path('logout/', logout_user, name='logout'),
]

