from django.db import models

# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    text = models.TextField(blank=True, verbose_name='Содержание')
    image = models.ImageField(upload_to='images/%Y-%m-%d/', verbose_name='Изображение')
    tags = models.ManyToManyField('Tag', verbose_name='Теги')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Новость'
        verbose_name = 'Новости'
        ordering = ('-created',)

    def __str__(self) -> str:
        return f'#{self.id} {self.title}' 


class Tag(models.Model):
    name = models.CharField(max_length=255, verbose_name='Наименование тега')

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
    
    def __str__(self) -> str:
        return self.name 