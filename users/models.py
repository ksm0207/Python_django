import uuid
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.mail import send_mail
from django.utils.html import strip_tags
from django.template.loader import render_to_string
from django.shortcuts import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):

    """ Custom User Model """

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, _("Male")),
        (GENDER_FEMALE, _("Female")),
        (GENDER_OTHER, _("Other")),
    )

    LANGUAGE_ENGLISH = "영어"
    LANGUAGE_KOREAN = "한국어"
    LANGUAGE_CHINA = "중국어"
    LANGUAGE_JAPAN = "일본어"

    LANGUAGE_CHOICES = (
        (LANGUAGE_ENGLISH, _("영어")),
        (LANGUAGE_KOREAN, _("한국어")),
        (LANGUAGE_CHINA, _("중국어")),
        (LANGUAGE_JAPAN, _("일본어")),
    )

    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"

    CURRENCY_CHOICES = (
        (CURRENCY_USD, "USD"),
        (CURRENCY_KRW, "KRW"),
    )

    LOGIN_EMAIL = "email"
    LOGIN_GITHUB = "Github"
    LOGIN_KAKAO = "Kakao"

    LOGIN_CHOICES = (
        (LOGIN_EMAIL, "email"),
        (LOGIN_GITHUB, "Github"),
        (LOGIN_KAKAO, "Kakao"),
    )

    avatar = models.ImageField(upload_to="avatars", blank=True)
    gender = models.CharField(
        _("gender"), blank=True, choices=GENDER_CHOICES, max_length=10,
    )
    bio = models.TextField(_("bio"), blank=True)
    birthday = models.DateField(blank=True, null=True)
    language = models.CharField(
        _("language"),
        blank=True,
        choices=LANGUAGE_CHOICES,
        max_length=25,
        default=LANGUAGE_KOREAN,
    )
    currency = models.CharField(
        blank=True, choices=CURRENCY_CHOICES, max_length=3, default=CURRENCY_KRW
    )
    superhost = models.BooleanField(default="False")
    email_verified = models.BooleanField(default=True)
    email_secret = models.CharField(max_length=20, default="", blank=True)
    login_method = models.CharField(
        max_length=50, choices=LOGIN_CHOICES, default=LOGIN_EMAIL
    )

    def get_absolute_url(self):
        return reverse("users:profile", kwargs={"pk": self.pk})

    def verify_email(self):
        if self.email_verified is False:
            secret = uuid.uuid4().hex[:20]
            self.email_secret = secret
            html_message = render_to_string(
                "emails/verify_email.html", {"secret": secret}
            )
            send_mail(
                _("이메일 테스트"),
                strip_tags(html_message),
                settings.EMAIL_FROM,
                [self.email],
                fail_silently=False,
                html_message=html_message,
            )
            self.save()
        return
