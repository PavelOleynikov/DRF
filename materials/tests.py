from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from materials.models import Course, Lesson
from users.models import User, Subscription


class LessonsTestCase(APITestCase):
    """Класс для тестирования CRUD уроков"""

    def setUp(self):
        self.user = User.objects.create(email="admin@sky.pro")
        self.course = Course.objects.create(name="python", description="backend", owner=self.user)
        self.lesson = Lesson.objects.create(name="циклы", course=self.course, owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_lesson_retrieve(self):
        """Тест получения конкретного урока"""

        url = reverse("materials:lesson-get", args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )
        self.assertEqual(data.get("name"), self.lesson.name)

    def test_lesson_valid_create(self):
        """Тест создания урока"""

        url = reverse("materials:lesson-create")
        data = {
            "name": "Списки",
            "description": "good",
            "link": "https://www.youtube.com/",
            "course": self.course.pk,
        }
        response = self.client.post(url, data)
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
        )
        self.assertEqual(
            Lesson.objects.all().count(),
            2,
        )

    def test_lesson_invalid_create(self):
        """Тест invalid создания урока"""

        url = reverse("materials:lesson-create")
        data = {
            "name": "Функции",
            "description": "good",
            "link": "https://www.you.com/",
            "course": self.course.pk,
        }
        response = self.client.post(url, data)
        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST,
        )

    def test_lesson_update(self):
        """Тест редактирования урока"""

        url = reverse("materials:lesson-update", args=(self.lesson.pk,))
        data = {
            "name": "Списки",
            "description": "good",
            "link": "https://www.youtube.com/",
            "course": self.course.pk,
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )
        self.assertEqual(data.get("name"), "Списки")

    def test_lesson_delete(self):
        """Тест удаления урока"""

        url = reverse("materials:lesson-delete", args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT,
        )
        self.assertEqual(
            Lesson.objects.all().count(),
            0,
        )

    def test_lesson_list(self):
        """Тест списка уроков"""

        url = reverse("materials:lesson-list")
        response = self.client.get(url)
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )


class SubscriptionTestCase(APITestCase):
    """Класс для тестирования подписок на курсы"""

    def setUp(self):
        self.user = User.objects.create(email="admin@sky.pro")
        self.course = Course.objects.create(name="python", description="backend", owner=self.user)
        self.client.force_authenticate(user=self.user)
        self.subscribe_url = reverse("users:subscribe")
        self.courses_list_url = reverse("materials:courses-list")
        self.course_detail_url = reverse("materials:courses-detail", args=(self.course.pk,))

    def test_subscribe_add(self):
        """Тест добавления подписки"""

        data = {"course_id": self.course.pk}
        response = self.client.post(self.subscribe_url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["message"], "Подписка добавлена")
        self.assertTrue(Subscription.objects.filter(user=self.user, course=self.course).exists())

    def test_subscribe_remove(self):
        """Тест удаления подписки"""

        Subscription.objects.create(user=self.user, course=self.course)
        self.assertEqual(Subscription.objects.count(), 1)

        data = {"course_id": self.course.pk}
        response = self.client.post(self.subscribe_url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["message"], "Подписка удалена")
        self.assertEqual(Subscription.objects.count(), 0)
