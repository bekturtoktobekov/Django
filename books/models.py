from django.db import models

class Books(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название книги')
    description = models.TextField(verbose_name='Описание книги')
    image = models.ImageField(upload_to='')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title