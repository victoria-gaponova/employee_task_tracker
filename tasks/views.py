from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from tasks.models import Task
from tasks.pagination import TaskPagination
from tasks.serializers import TaskSerializer
from users.models import Employee
from users.serializers import EmployeeSerializer


class TaskViewSet(viewsets.ModelViewSet):
    """
    Представление для взаимодействия с моделью задачи.

    Attributes:
        queryset (QuerySet): Набор данных задач, используемых в представлении.
        serializer_class (TaskSerializer): Сериализатор для задач.
        pagination_class (TaskPagination): Класс пагинации для данного представления.

    Methods:
        important_tasks: Пользовательское действие для получения важных задач.

    """

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    pagination_class = TaskPagination

    @action(detail=False, methods=["get"])
    def important_tasks(self, request):
        """
        API-метод для получения важных задач с информацией о потенциальных исполнителях.

        Parameters:
            request: Запрос от клиента.

        Returns:
            Response: JSON-ответ с информацией о важных задачах и их потенциальных исполнителях.
        """
        # Получаем задачи,которые соответствуют заданным критериям важных задач
        important_tasks = Task.objects.filter(
            status="не взята в работу", parent_task__status="в работе"
        )
        # Список для хранения информации о важных задачах и их потенциальных исполнителях.
        important_tasks_data = []

        for task in important_tasks:
            employees = Employee.objects.all()

            # Формируем словарь с количеством задач для каждого сотрудника.
            employee_tasks_count = {
                employee.id: Task.objects.filter(employee=employee).count()
                for employee in employees
            }

            # Находим минимальное количество задач среди всех сотрудников.
            least_busy_employee_tasks_count = min(
                employee_tasks_count.values(), default=0
            )

            # Список потенциальных исполнителей для текущей задачи.
            potential_employees = []

            # Проверка родительской задачи и её исполнителя.
            if task.parent_task and task.parent_task.employee:
                parent_employee = task.parent_task.employee
                parent_employee_tasks_count = employee_tasks_count.get(
                    parent_employee.id, 0
                )

                # Приоритет сотруднику,исполняющему родительскую задачу , если его нагрузка не превышает минимальную + 2 задачи
                if parent_employee_tasks_count < least_busy_employee_tasks_count + 2:
                    potential_employees.append(parent_employee)

            # Добавляем других сотрудников, если родительская задача не определена или их нагрузка минимальна
            if not potential_employees:
                potential_employees = [
                    employee
                    for employee in employees
                    if employee_tasks_count[employee.id] < least_busy_employee_tasks_count + 2
                ]

            # Формирование данных для ответа
            important_tasks_data.append(
                {
                    "Важная задача": task.name,
                    "Срок": task.deadline,
                    "Сотрудники": [employee.full_name for employee in potential_employees],
                }
            )

        return Response(important_tasks_data)
