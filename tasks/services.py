import os

import requests


def sending_notifications_to_telegram(task):
    """Отправление уведомления сотруднику о задаче в телеграм"""
    # Формируем текст уведомления
    text = f"Вам назначена задача {task.name}, дедлайн {task.deadline}"
    # Формируем URL для отправки сообщения в телеграм
    url = (
        f"https://api.telegram.org/bot"
        f"{os.getenv('TELEGRAM_API_TOKEN')}/sendMessage?chat_id={task.employee.chat_id}&text={text}"
    )
    # Отправляем запрос на API телеграма сформированным URL и получаем ответ в формате JSON
    response = requests.get(url).json()
    if response["ok"]:
        print("Уведомление успешно отправлено")
    else:
        print("Ошибка при отправке уведомления:", response["description"])
