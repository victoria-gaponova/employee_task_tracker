import os
from django.core.management.base import BaseCommand
from users.models import Employee


class Command(BaseCommand):
    help = "Create a new superuser"

    def handle(self, *args, **kwargs):
        super_user = Employee.objects.create(
            email=os.getenv("EMAIL_HOST_USER"),
            full_name="admin",
            position="position",
            is_staff=True,
            is_superuser=True,
            chat_id=os.getenv("CHAT_ID_ADMIN"),
        )
        super_user.set_password(os.getenv("ADMIN_PASSWORD"))
        super_user.save()
        self.stdout.write(self.style.SUCCESS(f"Superuser created successfully"))
