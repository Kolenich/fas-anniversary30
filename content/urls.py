"""Файл маршрутов приложения content."""

from django.urls import path

from .views import IndexView

app_name = 'content'

urlpatterns = [
    # Главная страница приложения со списком постов
    path(r'', IndexView.as_view(), name='index'),
]
