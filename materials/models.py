from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название")
    image = models.ImageField(upload_to="courses/", verbose_name="Картинка", null=True, blank=True)
    description = models.TextField(null=True, blank=True, verbose_name="Описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название")
    image = models.ImageField(upload_to="lessons/", verbose_name="Картинка", null=True, blank=True)
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    link = models.URLField(verbose_name="Ссылка на видео", null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="lessons", verbose_name="Курс")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
