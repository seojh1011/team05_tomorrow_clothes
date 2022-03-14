from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    nick_name = models.CharField(max_length=30)
