from django.utils import timezone
from rest_framework import serializers


def validate_deadline(data):
    """
    Валидатор для проверки срока выполнения задачи.
    Проверяет, что срок выполнения не раньше текущей даты.

    Args:
        data (dict): Словарь данных задачи, включая поле 'deadline'.

    Raises:
        serializers.ValidationError: Возникает, если срок выполнения задачи раньше текущей даты.

    Returns:
        None
    """
    deadline = data.get("deadline")
    if deadline and deadline < timezone.now().date():
        raise serializers.ValidationError(
            "Срок выполнения не может быть раньше текущей даты."
        )


def validate_name_lenght(data):
    """
    Валидатор для проверки длины наименования задачи.

    Args:
        data (dict): Словарь данных задачи, включая поле 'name'.

    Raises:
        serializers.ValidationError: Возникает, если наименование задачи содержит менее 3 символов.

    Returns:
        None
    """
    name = data.get("name")
    if len(name) < 3:
        raise serializers.ValidationError(
            "Наименование задачи должно содержать не менее 3 символов."
        )
