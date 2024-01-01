from django.contrib.auth.models import AbstractUser
from django.db import models


class EmployeeUser(AbstractUser):
    """
        Модель сотрудника с дополнительными полями.

        Дополнительные поля: employee_id, full_name, position, chat_id.

        Поля,унаследованные от AbstractUser: email.

        Attributes:
            employee_id (str): Идентификатор сотрудника.
            full_name (str): ФИО сотрудника.
            email (str): Уникальный адрес электронной почты сотрудника.
            position (str): Должность сотрудника.
            chat_id(str): id чата в tg
        """
    employee_id = models.CharField(max_length=10, unique=True, verbose_name='идентификатор сотрудника')
    username = None
    full_name = models.CharField(max_length=255, default= 'undefined',verbose_name='ФИО')
    email = models.EmailField(
        unique=True, verbose_name='электронная почта сотрудника'
    )
    position = models.CharField(max_length=50, verbose_name='должность')
    chat_id = models.CharField(
        max_length=20, unique=True, default=0, verbose_name="id пользователя в телеграм"
    )
    is_busy = models.BooleanField(default=False, help_text="признак занятости сотрудника")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


