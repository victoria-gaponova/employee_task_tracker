from django.contrib.auth.models import AbstractUser
from django.db import models


class Employee(AbstractUser):
    """
    Расширенная модель пользователя для представления сотрудников.

    Attributes:
        username (None): Поле username устанавливается в None, так как в данной модели
                         мы используем email в качестве уникального идентификатора пользователя.
        full_name (str): Полное имя сотрудника.
        email (str): Уникальный адрес электронной почты сотрудника.
        position (str): Должность сотрудника.
        chat_id (str): Идентификатор сотрудника в Telegram.

    USERNAME_FIELD:
        Поле email используется в качестве уникального идентификатора для входа в систему.

    REQUIRED_FIELDS:
        Поле, необходимое для создания суперпользователя. В данном случае, не требуется
        дополнительных полей для создания суперпользователя.

    """

    username = None
    full_name = models.CharField(
        max_length=255, default="undefined", verbose_name="ФИО"
    )
    email = models.EmailField(unique=True, verbose_name="электронная почта сотрудника")
    position = models.CharField(max_length=50, verbose_name="должность")
    chat_id = models.CharField(
        max_length=20,
        unique=True,
        default="",
        verbose_name="идентификатор сотрудника в Telegram",
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Employee"
