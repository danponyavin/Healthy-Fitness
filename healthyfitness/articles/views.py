from django.shortcuts import render
from django.shortcuts import get_object_or_404
from articles.models import Article


def all_articles(request):
    titles_of_articles = Article.objects.all()
    return render(request, 'articles/articles.html', {
        'titlesOfArticles': titles_of_articles, 'title': 'Статьи'})


def health_articles(request):
    titles_of_articles = Article.objects.filter(category=1)
    return render(request, 'articles/articles_health.html', {
        'titlesOfArticles': titles_of_articles, 'title': 'Статьи про здоровье'})


def devices_articles(request):
    titles_of_articles = Article.objects.filter(category=3)
    return render(request, 'articles/articles_devices.html', {
        'titlesOfArticles': titles_of_articles, 'title': 'Статьи про девайсы'})


def food_articles(request):
    titles_of_articles = Article.objects.filter(category=4)
    return render(request, 'articles/articles_food.html', {
        'titlesOfArticles': titles_of_articles, 'title': 'Статьи про питание'})


def sport_articles(request):
    titles_of_articles = Article.objects.filter(category=2)
    return render(request, 'articles/articles_sport.html', {
        'titlesOfArticles': titles_of_articles, 'title': 'Статьи про спорт'})


def show_certain_article(request, art_slug):
    article = get_object_or_404(Article, slag=art_slug)
    return render(request, 'articles/certain_article.html', {
        'article': article})
