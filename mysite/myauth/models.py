from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    username = models.CharField(max_length=30, null=False)
    email = models.CharField(null=False, unique=True)
    password1 = models.CharField(null=False, default="12345")
    photo = models.ImageField(upload_to="uploads", default="uploads/anonimous.jpg")

    # Указываем поле для входа (вместо username)
    USERNAME_FIELD = 'email'

    # Обязательные поля при создании пользователя (username уже включен в AbstractUser)
    REQUIRED_FIELDS = ['name']  # Минимум одно поле

    def __str__(self):
        return self.username