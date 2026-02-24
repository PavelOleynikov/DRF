from datetime import datetime, timedelta

from celery import shared_task

from users.models import User


@shared_task
def block_inactive_users():
    """Задача для проверки периода не активности пользователей и их блокировки"""

    date_now = datetime.now()
    inactive_users = User.objects.filter(is_superuser=False, last_login__lt=date_now - timedelta(days=30))
    inactive_users.update(is_active=False)
