from django.urls import path
from .views import get_news_list, get_news_detail, get_news_by_tag, get_top_news
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', get_news_list, name='news-list'),
    path('news/<int:pk>/', get_news_detail, name='news-detail'),
    path('news/<str:slug>/', get_news_by_tag, name='get-news-by-tag'),
    path('news/top', get_top_news, name='top-news')
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
