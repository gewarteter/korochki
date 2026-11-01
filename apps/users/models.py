from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    fio = models.CharField(max_length=100)
    telefon = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
