from django.contrib.auth import get_user_model
from rest_framework import serializers


class EmployeeUserSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели сотрудника.

    Attributes:
        employee_id (str): Уникальный идентификатор сотрудника.
        full_name (str): ФИО сотрудника.
        email (str): Адрес электронной почты сотрудника.
        position (str): Должность сотрудника.
        chat_id (str): id чата сотрудника в telegram.

    """
    class Meta:
        model = get_user_model()
        fields = ['employee_id', 'full_name', 'email', 'position', 'chat_id']
