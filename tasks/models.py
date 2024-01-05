from django.db import models

from employee_task_tracker import settings

NULLABLE = {"blank": True, "null": True}


class Task(models.Model):
    """
    Модель задач.

    Attributes:
        STATUS_CHOICES (tuple): Кортеж опций статусов задачи.
        name (str): Наименование задачи.
        deadline (Date): Срок выполнения задачи.
        status (str): Статус задачи выбирается из опций в STATUS_CHOICES.
        parent_task (Task): Родительская задача, ссылается на саму модель Task.
        employee (Employee): Исполнитель задачи, связь с моделью Employee (пользовательской моделью).

    Methods:
        __str__: Метод, возвращающий строковое представление задачи (наименование задачи).

    """

    STATUS_CHOICES = (
        ("не взята в работу", "Не взята в работу"),
        ("в работе", "В работе"),
        ("завершена", "Завершена"),
    )

    name = models.CharField(max_length=255, verbose_name="наименование задачи")
    deadline = models.DateField(verbose_name="срок выполнения")
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default="не взята в работу",
        verbose_name="статус задачи",
    )
    parent_task = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        **NULLABLE,
        verbose_name="родительская задача"
    )
    employee = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        **NULLABLE,
        on_delete=models.CASCADE,
        related_name="tasks",
        verbose_name="исполнитель задачи"
    )

    def __str__(self):
        return self.name
