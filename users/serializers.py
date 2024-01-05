from rest_framework import serializers

from tasks.serializers import TaskSerializer
from users.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели сотрудника.

    Attributes:
        id (int): Уникальный идентификатор сотрудника.
        full_name (str): Полное имя сотрудника.
        email (str): Адрес электронной почты сотрудника.
        position (str): Должность сотрудника.
        chat_id (str): Идентификатор сотрудника в Telegram.

    Поле tasks:
        Список задач, связанных с текущим сотрудником.
    """

    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = Employee
        fields = ["id", "full_name", "email", "position", "chat_id", "tasks"]
