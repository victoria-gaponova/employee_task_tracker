from django.contrib.auth.models import AbstractUser
from django.db import models


class EmployeeUser(AbstractUser):
    """
        Модель сотрудника с доаолнительными полями.

        Дополнительные поля: employee_id, position, chat_id.

        Поля,унаследованные от AbstractUser: first_name, last_name, email.

        Attributes:
            employee_id (str): Идентификатор сотрудника.
            email (str): Уникальный адрес электронной почты пользователя.
            position (str): Должность сотрудника.
            chat_id(str): id чата в tg
        """
    employee_id = models.CharField(max_length=10, unique=True, verbose_name='идентификатор сотрудника')
    username = None
    email = models.EmailField(
        unique=True, verbose_name="электронная почта пользователя"
    )
    position = models.CharField(max_length=50, verbose_name='должность')
    chat_id = models.CharField(
        max_length=20, unique=True, default=0, verbose_name="id пользователя в телеграм"
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


