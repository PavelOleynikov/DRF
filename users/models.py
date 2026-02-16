from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Класс пользователя."""

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


class Payments(models.Model):
    """Класс для работы с платежами"""

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="payments", verbose_name="пользователь")
    payment_date = models.DateTimeField(auto_now_add=True, verbose_name="дата платежа")
    paid_course = models.ForeignKey(
        "materials.Course", on_delete=models.CASCADE, related_name="paid_course", verbose_name="оплаченный курс"
    )
    paid_lesson = models.ForeignKey(
        "materials.Lesson", on_delete=models.CASCADE, related_name="paid_lesson", verbose_name="оплаченный урок"
    )
    amount = models.DecimalField(verbose_name="сумма оплаты", max_digits=10, decimal_places=2)
    method_payment = models.CharField(
        max_length=10,
        choices=[("cash", "Наличные"), ("transfer", "Перевод на счет")],
        verbose_name="Способ оплаты",
        help_text="Выберите способ оплаты",
    )

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"
        ordering = ["-payment_date"]
        unique_together = ["user", "paid_course", "paid_lesson"]

    def __str__(self):
        return f"{self.user} - {self.paid_course} - {self.paid_lesson}"


class Subscription(models.Model):
    """Класс подписки пользователя на курс"""

    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="subscription", verbose_name="пользователь"
    )
    course = models.ForeignKey(
        "materials.Course", on_delete=models.CASCADE, related_name="subscription", verbose_name="подписка на курс"
    )
    subscription_date = models.DateTimeField(auto_now_add=True, verbose_name="дата подписки")

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"
        ordering = ["-subscription_date"]
        unique_together = ["user", "course"]

    def __str__(self):
        return f"{self.user.email} - подписан на {self.course.name}"
