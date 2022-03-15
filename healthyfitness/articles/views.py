from django.shortcuts import render



def allArticles(request):
    return render(request, 'articles/articles.html', {'title': 'Статьи'})


def healthArticles(request):
    return render(request, 'articles/articles_health.html', {'title': 'Статьи про здоровье'})


def devicesArticles(request):
    return render(request, 'articles/articles_devices.html', {'title': 'Статьи про девайсы'})


def foodArticles(request):
    return render(request, 'articles/articles_food.html', {'title': 'Статьи про питание'})


def sportArticles(request):
    return render(request, 'articles/articles_sport.html', {'title': 'Статьи про спорт'})
