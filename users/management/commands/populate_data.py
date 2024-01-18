from django.core.management.base import BaseCommand

from faker import Faker

from users.models import Employee


class Command(BaseCommand):
    help = "Generates fake data for employees"

    def handle(self, *args, **kwargs):
        faker = Faker()
        Employee.objects.all().delete()

        for _ in range(10):  # Количество сотрудников для создания
            Employee.objects.create(
                full_name=faker.name(),
                email=faker.email(),
                position=faker.job(),
                chat_id=faker.lexify(text="????????????????????"),
            )

        self.stdout.write(
            self.style.SUCCESS("Successfully populated the database with fake data")
        )
