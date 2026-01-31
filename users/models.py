from django.contrib.auth.models import AbstractUser
from django.db import models

from materials.models import Course, Lesson


class User(AbstractUser):

    username = None

    email = models.EmailField(verbose_name="почта", unique=True)
    phone_number = models.CharField(verbose_name="номер телефона", max_length=15, blank=True, null=True)
    avatar = models.ImageField(verbose_name="аватар", upload_to="avatars/", blank=True, null=True)
    city = models.CharField(verbose_name="страна", max_length=50, blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class Payments(models.Model):
    """Класс для работы с платежами"""

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="payments", verbose_name="пользователь")
    payment_date = models.DateTimeField(auto_now_add=True, verbose_name="дата платежа")
    paid_course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="paid_course", verbose_name="оплаченный курс"
    )
    paid_lesson = models.ForeignKey(
        Lesson, on_delete=models.CASCADE, related_name="paid_lesson", verbose_name="оплаченный урок"
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
