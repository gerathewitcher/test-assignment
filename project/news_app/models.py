from django.db import models
from django.urls import reverse
from django.utils import tree


# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    text = models.TextField(blank=True, verbose_name='Содержание')
    image = models.ImageField(
        upload_to='images/%Y-%m-%d/', verbose_name='Изображение')
    tags = models.ManyToManyField(
        'Tag', verbose_name='Теги', related_name='news')
    views = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ('-created',)

    def __str__(self) -> str:
        return f'#{self.id} {self.title}'

    def get_absolute_url(self):
        return reverse('news-detail', kwargs={'pk': self.pk})


class Tag(models.Model):
    name = models.CharField(max_length=255, verbose_name='Наименование тега')
    slug = models.SlugField(verbose_name='Slug(Заполняется автоматически)')

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse('get-news-by-tag', kwargs={'slug': self.slug})
