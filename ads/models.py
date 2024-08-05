from django.conf import settings
from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Ad(models.Model):
    title = models.CharField(max_length=100, verbose_name='название товара')
    price = models.PositiveIntegerField(verbose_name='цена ')
    description = models.TextField(verbose_name='описание')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='продавец')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания объявления')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'объявление'
        verbose_name_plural = 'объявления'
        ordering = ('-created_at',)


class Comment(models.Model):
    text = models.TextField(verbose_name='текст отзыва')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='автор отзыва')
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, related_name='comments', verbose_name='объявление')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания отзыва')

    def __str__(self):
        return f'{self.author} ({self.created_at})'

    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'отзывы'
        ordering = ('-created_at',)
