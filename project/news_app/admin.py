from django.contrib import admin
from django.contrib.admin.decorators import display
from django.db import models
from .models import News, Tag

# Register your models here.


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',), }


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'image', 'created')
