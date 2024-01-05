from rest_framework import serializers

from tasks.models import Task
from tasks.validators import validate_deadline, validate_name_lenght


class TaskSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели задачи.

    Attributes:
        name (str): Наименование задачи.
        deadline (Date): Срок выполнения задачи.
        status (str): Статус задачи.
        parent_task (int): Идентификатор родительской задачи (ForeignKey).
        employee (int): Идентификатор исполнителя задачи (ForeignKey).

    """

    class Meta:
        model = Task
        fields = ["id", "name", "deadline", "status", "parent_task", "employee"]

    def validate(self, data):
        validate_deadline(data)
        validate_name_lenght(data)
        return data
