from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.mail import EmailMessage
from django.core.validators import RegexValidator
from django.db import models
from django.template.loader import render_to_string # txt file read 

# User을 modeling 하기위해 AbstractUser을 상속 -> admin 사이트 연결
class User(AbstractUser):
    class GenderChoices(models.TextChoices):
        MALE = "M", "남"
        FEMALE = "F","여"

    website_url = models.URLField(max_length=200, blank=True)
    bio = models.TextField(blank=True)
    phone_number = models.CharField(max_length=13, blank=True, validators=[RegexValidator(r"^010-?[1-9]/d(3)-?/d(4)$")])
    gender = models.CharField(max_length=1, blank=True,choices=GenderChoices.choices) # django 3 Semantics
    avatar = models.ImageField(blank=True, upload_to="%Y")

    def send_welcome_email(self):
        title = render_to_string("accounts/welcome_email_title.txt",{"user":self})
        body = render_to_string("accounts/welcome_email_body.txt",{"user":self})
        to_email = [self.email]
        email = EmailMessage(
            title,      # title
            body,       # body
            settings.WELCOME_EMAIL_SENDER,     # 보내는 이메일 setting -> ADMIN 참조
            to=to_email,  # 받는 이메일 리스트
        )
        email.send()