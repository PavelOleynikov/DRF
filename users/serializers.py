from rest_framework import serializers

from users.models import Payments


class PaymentsSerializer(serializers.ModelSerializer):
    """Сериализатор для работы с платежами"""

    class Meta:
        model = Payments
        fields = "__all__"
