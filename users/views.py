from rest_framework import generics

from users.models import EmployeeUser
from users.serializers import EmployeeUserSerializer


class EmployeeUserListCreateView(generics.ListCreateAPIView):
    """Представление для создания  и просмотра списка задач сотрудника.
    Attributes:
        queryset (QuerySet): Набор объектов задач.
        serializer_class (EmployeeUserSerializer): Сериализатор, используемый для преобразования объектов задач в JSON.
    """
    queryset = EmployeeUser.objects.all()
    serializer_class = EmployeeUserSerializer


class EmployeeUserDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Представление для просмотра, обновления и удаления задачи
    Attributes:
        queryset (QuerySet): Набор объектов задач.
        serializer_class (LessonSerializer): Сериализатор, используемый для преобразования объектов задач в JSON.
    """
    queryset = EmployeeUser.objects.all()
    serializer_class = EmployeeUserSerializer