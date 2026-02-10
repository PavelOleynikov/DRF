from rest_framework import viewsets
from rest_framework.generics import CreateAPIView

from users.models import User
from users.serializers import UserCreateSerializer, UserDetailViewSerializer, UserViewSerializer


class UserCreateAPIView(CreateAPIView):
    """Создание пользователя"""

    serializer_class = UserCreateSerializer
    queryset = User.objects.all()

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserViewSet(viewsets.ModelViewSet):
    """Класс для работы с пользователями"""

    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.action == "retrieve":
            return UserDetailViewSerializer
        return UserViewSerializer
