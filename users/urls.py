from django.urls import path

from users.apps import UsersConfig
from users.views import EmployeeUserListCreateView, EmployeeUserDetailView, BusyEmployeesUserListView

app_name = UsersConfig.name

urlpatterns = [
    path('employees/', EmployeeUserListCreateView.as_view(), name='employee-list-create'),
    path('<int:pk>/employee/', EmployeeUserDetailView.as_view(), name='employee-detail'),
    path('employees/busy/', BusyEmployeesUserListView.as_view(), name='employee_busy-list')
]