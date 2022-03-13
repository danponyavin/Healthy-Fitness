from django.shortcuts import render


def main_page(request):
    return render(request, 'main/main_page.html', {'title': 'Главная'})


def articles(request):
    return render(request, 'articles/articles.html', {'title': 'Статьи'})


def calculator(request):
    return render(request, 'main/calculator.html', {'title': 'Калькулятор'})


def blog(request):
    return render(request, 'main/blog.html', {'title': 'Блог'})


def personal_area(request):
    return render(request, 'main/personal_area.html', {'title': 'Личный кабинет'})


def registration_field(request):
    return render(request, 'registration/registration_field.html', {'title': 'Регистрация'})
