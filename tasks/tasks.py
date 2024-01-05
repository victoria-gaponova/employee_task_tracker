from celery import shared_task

from tasks.models import Task
from tasks.services import sending_notifications_to_telegram


@shared_task
def send_message():
    # Получаем все задачи с текущим статусом "в работе" из модели Task
    tasks = Task.objects.filter(status="в работе")
    for task in tasks:
        sending_notifications_to_telegram(task)
