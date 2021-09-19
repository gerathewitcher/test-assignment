from django.shortcuts import get_object_or_404, render
from .models import News, Tag
from django.views.generic import ListView


# Create your views here.

def get_news_list(request):
    """Главная страница, возвращает список всех новостей"""
    news = News.objects.all()

    return render(request, 'news_list.html', {'news_list': news})


def get_news_detail(request, pk):
    """Страница новости, возвращает конкретную новость"""

    news = get_object_or_404(News, id=pk)
    news.views = news.views + 1
    news.save()

    return render(request, 'news_detail.html', {'news': news})


def get_news_by_tag(request, slug):
    """Страница новостей по тегу"""

    news_list = News.objects.filter(tags__slug=slug)

    return render(request, 'news_by_tag.html', {'news_list': news_list})


def get_top_news(request):
    """Страница с топ новостями, а так же общим кол-вом просмотров"""

    top_news = News.objects.all().order_by('-views')

    total_views = [news.views for news in top_news]

    return render(request, 'top_news.html', {'top_news': top_news, 'total_views': sum(total_views)})
