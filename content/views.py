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
        navbar_links = [
            {'name': 'Обращение', 'width': '126px', 'href': '#appeal'},
            {'name': 'Хроника', 'width': '111px', 'href': '#chronicle'},
            {'name': 'История', 'width': '103px', 'href': '#history'},
            {'name': '10 законов', 'width': '123px', 'href': '#ten-laws'},
            {'name': 'Прямая речь', 'width': '134px', 'href': '#direct-speech'},
            {'name': 'Видео поздравления', 'width': '189px', 'href': '#video-congratulation'},
            {'name': 'Итоги', 'width': '80px', 'href': '#summary'},
            {'name': 'Музей', 'width': '83px', 'href': '#museum-materials-reports'},
            {'name': 'Материалы', 'width': '117px', 'href': '#museum-materials-reports'},
            {'name': 'Доклады', 'width': '104px', 'href': '#museum-materials-reports'},
        ]
        context = super().get_context_data(**kwargs)
        context.update({
            'books': Book.objects.all(),
            'videos': Video.objects.all(),
            'documents': Document.objects.all(),
            'photo_cards': PhotoCard.objects.all(),
            'infographics': Infographics.objects.all(),
            'magazines': Magazine.objects.all(),
            'navbar_links': navbar_links
        })
        return context
