# Generated by Django 4.2.9 on 2024-01-05 21:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0003_alter_employee_options_remove_employee_is_busy"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employee",
            name="chat_id",
            field=models.CharField(
                default="",
                max_length=20,
                unique=True,
                verbose_name="идентификатор сотрудника в Telegram",
            ),
        ),
    ]
