from django.db import models
from django.contrib.auth.models import AbstractUser
from app.choices import *


# Create your models here.
class User(AbstractUser):
    user_type = models.CharField(
        max_length=1, choices=USER_CHOICES, default='U')

    def __str__(self):
        return self.email
