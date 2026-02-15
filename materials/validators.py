from rest_framework.serializers import ValidationError

valid_link = "youtube.com"


def validate_link(value):
    """
    Проверка валидности ссылки
    """

    if valid_link not in value:
        raise ValidationError("Ссылка должна быть в формате youtube.com")
