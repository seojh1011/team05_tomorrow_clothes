from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Meta:
        db_table = "TOMORROW_USER"

    nick_name = models.CharField(max_length=50, default="kakao")
    pro_img_url = models.FileField(upload_to="images", blank=True, null=True, default="images/cat01.jpg")
