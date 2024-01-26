from django.db import models

class Movies(models.Model):
    CATEGORIES = (
        ('Боевик', 'Боевик'),
        ('Драма', 'Драма'),
        ('Комедия', 'Комедия'),
        ('Романтика', 'Романтика'),
        ('Научная фантастика (Sci-Fi)', 'Научная фантастика (Sci-Fi)'),
        ('Фэнтези', 'Фэнтези'),
        ('Детектив', 'Детектив'),
        ('Триллер', 'Триллер'),
        ('Документальный', 'Документальный'),
    )
    name = models.CharField(max_length=20, verbose_name='Укажите название фильма')
    description = models.TextField(verbose_name='Укажите описание', blank=True, null=True)
    image = models.URLField(verbose_name='Вставьте ссылку на фото')
    genre = models.CharField(max_length=100, choices=CATEGORIES, verbose_name='Выберите жанр')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Review(models.Model):
    CHOICES = (
        (1, '1 звезда'),
        (2, '2 звезды'),
        (3, '3 звезды'),
        (4, '4 звезды'),
        (5, '5 звезд'),
    )
    text = models.TextField(verbose_name='Введите комментарий')
    stars = models.PositiveIntegerField(choices=CHOICES, default=5, verbose_name='Поставьте звезду')


    def __str__(self):
        return f'{self.stars}\n{self.text}'
