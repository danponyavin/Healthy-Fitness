from django.shortcuts import render


def registration_field(request):
    return render(request, 'registration/registration_field.html')


def login(request):
    return render(request, 'registration/login.html')

