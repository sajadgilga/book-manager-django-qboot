from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from users.models import BaseModel

User = get_user_model()


class Book(BaseModel):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    text = models.TextField()
