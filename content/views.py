"""Представления для приложения posts_app."""

from django.views.generic import ListView

from content.models import Book, Booklet, Document, Infographics, Magazine, PhotoCard, Video


class IndexView(ListView):
    """Корневое представление главной страницы."""

    template_name = 'index.html'
    model = Booklet
    context_object_name = 'booklets'

    def get_context_data(self, **kwargs):
        """Переопределение метода передачи в шаблон контекста. Добавляет остальные кверисеты по моделям."""
        context = super().get_context_data(**kwargs)
        context.update({
            'books': Book.objects.all(),
            'videos': Video.objects.all(),
            'documents': Document.objects.all(),
            'photo_cards': PhotoCard.objects.all(),
            'infographics': Infographics.objects.all(),
            'magazines': Magazine.objects.all(),
        })
        return context
