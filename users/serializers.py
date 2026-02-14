from rest_framework.serializers import ModelSerializer

from users.models import Payments, User


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
