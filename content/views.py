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
        context.update({
            'booklets': Booklet.objects.all(),
            'books': Book.objects.all(),
            'videos': Video.objects.all(),
            'documents': Document.objects.all(),
            'photo_cards': PhotoCard.objects.all(),
            'infographics': Infographics.objects.all(),
            'magazines': Magazine.objects.all(),
            **vars(extra_context)
        })
        return context
