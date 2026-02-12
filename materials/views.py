from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated

from materials.models import Course, Lesson
from materials.serializers import CourseSerializer, LessonSerializer
from users.permissions import ModeratorPermissions


class CourseViewSet(viewsets.ModelViewSet):
    """Класс для работы с курсами"""

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ["name"]
    ordering_fields = ["name"]
    ordering = ["-name"]

    def perform_create(self, serializer):
        course = serializer.save()
        course.owner = self.request.user
        course.save()

    def get_permissions(self):
        if self.action in ["create", "destroy"]:
            self.permission_classes = [IsAuthenticated, ~ModeratorPermissions]
        elif self.action in ["update", "retrieve"]:
            self.permission_classes = [IsAuthenticated, ModeratorPermissions]
        return super().get_permissions()


class LessonCreateAPIView(generics.CreateAPIView):
    """Класс для создания урока"""

    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, ~ModeratorPermissions]

    def perform_create(self, serializer):
        lesson = serializer.save()
        lesson.owner = self.request.user
        lesson.save()


class LessonListAPIView(generics.ListAPIView):
    """Класс для получения списка уроков"""

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ["course"]
    ordering_fields = ["name"]
    ordering = ["-name"]


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    """Класс для получения конкретного урока"""

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonUpdateAPIView(generics.UpdateAPIView):
    """Класс для редактирования урока"""

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonDestroyAPIView(generics.DestroyAPIView):
    """Класс для удаления урока"""

    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, ~ModeratorPermissions]
