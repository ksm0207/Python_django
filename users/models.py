import uuid
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.mail import send_mail


class User(AbstractUser):

    """ Custom User Model """

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    LANGUAGE_ENGLISH = "영어"
    LANGUAGE_KOREAN = "한국어"
    LANGUAGE_CHINA = "중국어"
    LANGUAGE_JAPAN = "일본어"

    LANGUAGE_CHOICES = (
        (LANGUAGE_ENGLISH, "영어"),
        (LANGUAGE_KOREAN, "한국어"),
        (LANGUAGE_CHINA, "중국어"),
        (LANGUAGE_JAPAN, "일본어"),
    )

    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"

    CURRENCY_CHOICES = (
        (CURRENCY_USD, "USD"),
        (CURRENCY_KRW, "KRW"),
    )

    avatar = models.ImageField(upload_to="avatars", blank=True)
    bio = models.TextField(blank=True)
    birthday = models.DateField(blank=True, null=True)

    gender = models.CharField(blank=True, choices=GENDER_CHOICES, max_length=10,)
    language = models.CharField(
        blank=True, choices=LANGUAGE_CHOICES, max_length=25, default=LANGUAGE_KOREAN
    )
    currency = models.CharField(
        blank=True, choices=CURRENCY_CHOICES, max_length=3, default=CURRENCY_KRW
    )
    superhost = models.BooleanField(default="False")
    email_verified = models.BooleanField(default=False)
    email_secret = models.CharField(max_length=20, default="", blank=True)

    def verify_email(self):
        if self.email_verified is False:
            secret = uuid.uuid4().hex[:20]
            self.email_secret = secret
            send_mail(
                "My Email Test",
                f"Success!! : {secret}",
                settings.EMAIL_FROM,
                [self.email],
                fail_silently=False,
            )
        return
