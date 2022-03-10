from django.shortcuts import render


def main_page(request):
    return render(request, 'main/main_page.html')


def articles(request):
    return render(request, 'main/articles.html')


def calculator(request):
    return render(request, 'main/calculator.html')


def blog(request):
    return render(request, 'main/blog.html')


def food_diary(request):
    return render(request, 'main/food_diary.html')


def personal_area(request):
    return render(request, 'main/personal_area.html')


def registration_field(request):
    return render(request, 'registration/registration_field.html')
