from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    phone_number = models.CharField(max_length=12, unique=True)
    nick_name = models.CharField(max_length=32, null=True, blank=True)
    avatar = models.ImageField(upload_to='media/avatars', null=True, blank=True)
