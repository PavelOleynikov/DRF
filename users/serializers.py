from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from users.models import Payments, User


class PaymentsCreateSerializer(ModelSerializer):
    """Сериализатор для создания платежа"""

    class Meta:
        model = Payments
        fields = "__all__"

    def validate(self, data):
        """Валидация: должен быть указан либо курс, либо урок"""

        paid_course = data.get("paid_course")
        paid_lesson = data.get("paid_lesson")

        if not paid_course and not paid_lesson:
            raise serializers.ValidationError("Необходимо указать либо оплачиваемый курс, либо оплачиваемый урок")
        if paid_course and paid_lesson:
            raise serializers.ValidationError("Нельзя одновременно оплачивать курс и урок")
        return data


class PaymentsSerializer(ModelSerializer):
    """Сериализатор для работы с платежами"""

    class Meta:
        model = Payments
        fields = "__all__"


class UserCreateSerializer(ModelSerializer):
    """Сериализатор для создания пользователя"""

    class Meta:
        model = User
        fields = ["id", "email", "password"]


class UserDetailViewSerializer(ModelSerializer):
    """Сериализатор для отображения деталей пользователя"""

    class Meta:
        model = User
        fields = ["id", "email", "phone_number", "city", "avatar"]


class UserViewSerializer(ModelSerializer):
    """Сериализатор для отображения списка пользователей"""

    class Meta:
        model = User
        fields = ["id", "email", "phone_number"]
