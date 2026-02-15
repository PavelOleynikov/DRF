from rest_framework import serializers

from materials.models import Course, Lesson
from materials.validators import validate_link


class LessonSerializer(serializers.ModelSerializer):
    """Сериализатор для работы с уроками"""

    link = serializers.URLField(validators=[validate_link], required=False)

    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    """Сериализатор для работы с курсами"""

    lessons_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = "__all__"

    def get_lessons_count(self, obj):
        # Используем related_name "lessons" для доступа к урокам курса
        return obj.lessons.count()
