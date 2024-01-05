from django.contrib import admin

from users.models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "position")
    search_fields = ("full_name", "email", "position")
    list_filter = ("position",)
    ordering = ("full_name",)
    exclude = (
        "password",
        "first_name",
        "last_name",
        "is_active",
        "is_staff",
        "is_superuser",
        "groups",
        "user_permissions",
        "last_login",
        "date_joined",
    )
