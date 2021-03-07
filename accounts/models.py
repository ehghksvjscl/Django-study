from django.contrib.auth.models import AbstractUser
from django.db import models

# User을 modeling 하기위해 AbstractUser을 상속 -> admin 사이트 연결
class User(AbstractUser):
    website_url = models.URLField(max_length=200, blank=True)
    bio = models.TextField(blank=True)