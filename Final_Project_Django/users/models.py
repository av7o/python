from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=100)
    id_number = models.CharField(max_length=11, unique=True)
    faculty = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.full_name} ({self.id_number})"
