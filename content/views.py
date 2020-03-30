"""Представления для приложения posts_app."""

from django.views.generic import ListView

from content.models import Book


class IndexView(ListView):
    """Корневое представление главной страницы."""

    template_name = 'index.html'
    model = Book
    context_object_name = 'books'
