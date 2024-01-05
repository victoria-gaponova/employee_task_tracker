from django.db.models import Count, Q
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from users.models import Employee
from users.pagination import EmployeePagination
from users.serializers import EmployeeSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    """
    Представление для взаимодействия с моделью сотрудника.

    Attributes:
        queryset (QuerySet): Набор данных сотрудников, используемых в представлении.
        serializer_class (EmployeeSerializer): Сериализатор для сотрудников.
        pagination_class (EmployeePagination): Класс пагинации для данного представления.

    Methods:
        busy_employees: Пользовательское действие для получения списка занятых сотрудников.

    """

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class = EmployeePagination

    @action(detail=False, methods=["get"])
    def busy_employees(self, request):
        """
        Получение списка занятых сотрудников.

        Parameters:
            request (Request): Запрос от клиента.

        Returns:
            Response: JSON-ответ с информацией о занятых сотрудников.

        """
        employees = (
            Employee.objects.annotate(
                active_tasks_count=Count("tasks", filter=Q(tasks__status="в работе"))
            )
            .filter(active_tasks_count__gt=0)
            .order_by("-active_tasks_count")
        )
        serializer = self.get_serializer(employees, many=True)
        return Response(serializer.data)
