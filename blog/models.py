from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название блога')
    description = models.TextField(verbose_name='Описание бота')
    image = models.ImageField(upload_to='')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
