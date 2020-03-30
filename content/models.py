"""Файл с моделями для приложения content."""
from django.db import models


class Booklet(models.Model):
    """Класс модель буклетов."""

    file = models.FileField('Буклет', upload_to='booklets/files')
    preview = models.ImageField('Превью', upload_to='booklets/previews', blank=True, null=True)
    description = models.TextField('Описание')
    source = models.CharField('Источник', max_length=100)
    order = models.IntegerField('Последовательность отображения')
    name = models.CharField('Название', max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Буклет'
        verbose_name_plural = 'Буклеты'
        db_table = 'booklets'


class Book(models.Model):
    """Класс - модель книги."""

    file = models.FileField('Книга', upload_to='books')
    description = models.TextField('Описание')
    author = models.CharField('Автор', max_length=150)
    order = models.IntegerField('Последовательность отображения')
    name = models.CharField('Название', max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        db_table = 'books'


class Video(models.Model):
    """Модель для хранения видео для блока Прямая речь."""

    file = models.FileField('Видео прямой речи', upload_to='videos/files')
    img = models.ImageField('Картинка-превью для видео', upload_to='videos/previews')
    text = models.CharField('Краткое описание видео', max_length=65)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Видео запись'
        verbose_name_plural = 'Видео записи'
        db_table = 'videos'


class Document(models.Model):
    """Модель для хранения документов для блока Прямая речь."""

    file = models.FileField('Документ для блока прямая речь', upload_to='documents')
    title = models.CharField('Название документа', max_length=50)
    text = models.CharField('Текст-описание документа', max_length=150)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'
        db_table = 'documents'


class PhotoCard(models.Model):
    """Модель фотокарточки."""

    img = models.ImageField('Изображения фотокарточки', upload_to='photos')
    date = models.DateField('Дата создания изображения')
    sub_title = models.CharField('Краткое описание фотокарточки', max_length=70)
    text = models.TextField('Полное описание фотокарточки', blank=True, null=True)

    def __str__(self):
        return self.sub_title

    class Meta:
        verbose_name = 'Фотокарточка'
        verbose_name_plural = 'Фотокарточки'
        db_table = 'photo_cards'


class Infographics(models.Model):
    """Модель инфографики."""

    file = models.FileField('Буклет', upload_to='infographics/files')
    preview = models.ImageField('Превью', upload_to='infographics/previews', blank=True, null=True)
    description = models.TextField('Описание')
    source = models.CharField('Источник', max_length=100)
    order = models.IntegerField('Последовательность отображения')
    name = models.CharField('Название', max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Инфографика'
        verbose_name_plural = 'Инфографики'
        db_table = 'infographics'


class Magazine(models.Model):
    """Модель для храненя жрунала."""

    file = models.FileField('Журнал', upload_to='magazines')
    description = models.TextField('Описание журнала')
    publication = models.DateField('Дата выпуска')
    publishing_house = models.CharField('Издательство', max_length=100)
    order = models.IntegerField('Порядок отображения')
    name = models.CharField('Название журнала', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Журнал'
        verbose_name_plural = 'Журналы'
        db_table = 'magazines'
