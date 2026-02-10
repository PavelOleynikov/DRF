from rest_framework.serializers import ModelSerializer

from users.models import User


class UserCreateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "phone_number"]


class UserDetailViewSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "phone_number", "city", "avatar"]


class UserViewSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "phone_number"]
