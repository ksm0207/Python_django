from django.contrib.auth.models import AbstractUser
from django.db import models


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
    email_confirmed = models.BooleanField(default=False)
    email_secret = models.CharField(max_length=120, default="", blank=True)

    def verify_email(self):
        pass
