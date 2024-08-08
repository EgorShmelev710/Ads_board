from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    ROLES = [
        ("admin", "администратор"),
        ("user", "пользователь"),
    ]

    username = None
    email = models.EmailField(unique=True, verbose_name='email')
    first_name = models.CharField(max_length=100, verbose_name='имя')
    last_name = models.CharField(max_length=100, verbose_name='фамилия')
    phone = models.CharField(max_length=100, verbose_name='телефон', **NULLABLE)
    role = models.CharField(max_length=20, choices=ROLES, default='user')
    image = models.ImageField(upload_to='users/', verbose_name='аватарка', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email} - {self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
