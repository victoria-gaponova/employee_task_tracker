from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet

# Создаем экземпляр DefaultRouter
router = DefaultRouter()
# Регистрируем EmployeeViewSet с именем 'employees'
router.register(r"employees", EmployeeViewSet, basename="employee")

urlpatterns = [
    path("", include(router.urls)),
]
