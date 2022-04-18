from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from registration.forms import RegisterUserForm


def login(request):
    return render(request, 'registration/login.html')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'registration/registration_field.html'
    success_url = reverse_lazy('home')



