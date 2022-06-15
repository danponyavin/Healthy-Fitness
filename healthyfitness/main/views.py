from django.shortcuts import render
from articles.models import Article


def main_page(request):
    titlesNewArticles = Article.objects.order_by('-time_create')[:3]
    return render(request, 'main/main_page.html', {'titlesNewArticles': titlesNewArticles, 'title': 'Главная'})
