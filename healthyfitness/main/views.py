from django.shortcuts import render
from articles.models import *


def main_page(request):
    titlesNewArticles = Article.objects.order_by('-time_create')[:3]
    return render(request, 'main/main_page.html', {'titlesNewArticles' : titlesNewArticles,'title': 'Главная'})


def articles(request):
    return render(request, 'articles/articles.html', {'title': 'Статьи'})

def blog(request):
    return render(request, 'main/blog.html', {'title': 'Блог'})


def personal_area(request):
    return render(request, 'main/personal_area.html', {'title': 'Личный кабинет'})


def registration_field(request):
    return render(request, 'registration/registration_field.html', {'title': 'Регистрация'})
