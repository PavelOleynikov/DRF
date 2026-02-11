from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    username = None

    email = models.EmailField(verbose_name="почта", unique=True, help_text="введите почту")
    phone_number = models.CharField(
        verbose_name="номер телефона", max_length=15, blank=True, null=True, help_text="введите номер телефона"
    )
    avatar = models.ImageField(
        verbose_name="аватар", upload_to="avatars/", blank=True, null=True, help_text="загрузите аватар"
    )
    city = models.CharField(verbose_name="город", max_length=50, blank=True, null=True, help_text="введите город")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
