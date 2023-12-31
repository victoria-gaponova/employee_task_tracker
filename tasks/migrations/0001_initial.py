# Generated by Django 5.0 on 2024-01-03 18:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Task",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=255, verbose_name="наименование задачи"
                    ),
                ),
                ("deadline", models.DateField(verbose_name="срок выполнения")),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("не взята в работу", "Не взята в работу"),
                            ("в работе", "В работе"),
                            ("завершена", "Завершена"),
                        ],
                        default="не взята в работу",
                        max_length=50,
                        verbose_name="статус задачи",
                    ),
                ),
                (
                    "employee",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tasks",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="исполнитель задачи",
                    ),
                ),
                (
                    "parent_task",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="tasks.task",
                        verbose_name="родительская задача",
                    ),
                ),
            ],
        ),
    ]
