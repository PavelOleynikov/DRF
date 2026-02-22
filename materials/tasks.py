from celery import shared_task
from django.core.mail import send_mail

from config.settings import EMAIL_HOST_USER


@shared_task
def send_course_update_email(course_name, email):
    """Отправка письма об обновлении курса"""

    send_mail(
        f"Новое обновление курса: {course_name}",
        f"Курс '{course_name}' был обновлен. Зайдите посмотреть новые материалы!",
        EMAIL_HOST_USER,
        [email],
    )
