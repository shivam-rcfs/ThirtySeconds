from django.contrib import admin
from .models import Category, CategoryData


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(CategoryData)
class CategoryDataAdmin(admin.ModelAdmin):
    list_display = ['id', 'words', 'category']

