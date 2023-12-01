from django.db import models

class MangaListModel(models.Model):
    GENRE = (
        ('Комедия', 'Комедия'),
        ('Хоррор', 'Хоррор'),
        ('Драмма', 'Драмма')
    )
    title = models.CharField(max_length=100, verbose_name='Напишите название манги')
    image = models.ImageField(upload_to='films/', verbose_name='Добавьте фото')
    year = models.DateField(verbose_name='Укажите год выпуска')
    director = models.CharField(max_length=100, verbose_name='Укажите режисера')
    genre = models.CharField(max_length=100, choices=GENRE)
    description = models.TextField(blank=True, verbose_name='Описание манги')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Манга'
        verbose_name_plural = 'Манги'


class Afisha(models.Model):
    manga = models.CharField(max_length=100, verbose_name='Название манги Афиша')
    time = models.TimeField(verbose_name='Дата создания манги')
    area = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.manga


class Slider(models.Model):
    slide = models.URLField()

    def __str__(self):
        return self.slide

class ReviewModel(models.Model):
    STARS = (
        ('*', '*'),
        ('**', '**'),
        ('***', '***'),
        ('****', '****'),
        ('*****', '*****'),
    )
    manga_list = models.ForeignKey(MangaListModel, on_delete=models.CASCADE, related_name='manga_list_name')
    stars = models.CharField(max_length=20, choices=STARS)
    description =models.TextField()

    def __str__(self):
        return f'{self.manga_list} - {self.stars}'