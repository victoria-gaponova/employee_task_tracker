from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

# Создаем экземпляр DefaultRouter
router = DefaultRouter()
# Регистрируем TaskViewSet с именем 'tasks'
router.register(r"tasks", TaskViewSet, basename="task")

urlpatterns = [
    path("", include(router.urls)),
]
