"""Представления для приложения content."""

from django.views.generic import TemplateView

import content.extra_context as extra_context
from content.models import Book, Booklet, Document, Infographics, Magazine, PhotoCard, Video


class IndexView(TemplateView):
    """Корневое представление главной страницы."""

    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        """Переопределение метода передачи в шаблон контекста. Добавляет остальные кверисеты по моделям."""
        context = super().get_context_data(**kwargs)
        extra_data = {key: value for key, value in vars(extra_context).items() if not key.startswith('__')}
        context.update({
            'booklets': Booklet.objects.order_by('order'),
            'books': Book.objects.order_by('order'),
            'videos': Video.objects.order_by('-id'),
            'documents': Document.objects.order_by('-id'),
            'photo_cards': PhotoCard.objects.order_by('-id'),
            'infographics': Infographics.objects.order_by('order'),
            'magazines': Magazine.objects.order_by('order'),
            **extra_data
        })
        return context
