from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.hashers import make_password


class User(models.Model):
    email = models.EmailField(unique=True, null=False)
    photo = models.ImageField(upload_to="uploads", default="uploads/anonimous.jpg")


    def __str__(self):
        return self.email