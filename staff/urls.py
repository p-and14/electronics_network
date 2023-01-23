from django.urls import path

from staff.views import EmployeeCreateView, EmployeeLogin

urlpatterns = [
    path("signup", EmployeeCreateView.as_view(), name="employee_signup"),
    path("login", EmployeeLogin.as_view(), name="employee_login"),
]
