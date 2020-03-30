"""Представления для приложения content."""

from django.views.generic import TemplateView

from content.models import Book, Booklet, Document, Infographics, Magazine, PhotoCard, Video


class IndexView(TemplateView):
    """Корневое представление главной страницы."""

    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        """Переопределение метода передачи в шаблон контекста. Добавляет остальные кверисеты по моделям."""
        context = super().get_context_data(**kwargs)
        context.update({
            'booklets': Booklet.objects.order_by('order'),
            'books': Book.objects.order_by('order'),
            'videos': Video.objects.order_by('-id'),
            'documents': Document.objects.order_by('-id'),
            'photo_cards': PhotoCard.objects.order_by('-id'),
            'infographics': Infographics.objects.order_by('order'),
            'magazines': Magazine.objects.order_by('order'),
        })
        return context
