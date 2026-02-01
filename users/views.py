from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters

from users.models import Payments
from users.serializers import PaymentsSerializer


class PaymentsViewSet(viewsets.ModelViewSet):
    """Класс для работы с платежами (вывод списка платежей)"""

    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ["paid_course", "paid_lesson", "method_payment"]
    ordering_fields = ["payment_date"]
    ordering = ["-payment_date"]  # по умолчанию сортировка по дате оплаты по убыванию
