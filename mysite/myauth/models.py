from django.db import models

class User(models.Model):
    name = models.CharField(max_length=30, null=False)
    email = models.CharField(null=False)
    password = models.CharField(null=False)

    def __str__(self):
        return self.name