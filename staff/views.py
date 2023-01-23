from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from rest_framework import generics, status
from rest_framework.exceptions import AuthenticationFailed

from staff import serializers
from staff.models import Employee


class EmployeeCreateView(generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = serializers.EmployeeRegistrationSerializer


class EmployeeLogin(generics.GenericAPIView):
    def post(self, request):
        username = request.data["username"]
        password = request.data["password"]

        employee = authenticate(request, username=username, password=password)
        if not employee:
            raise AuthenticationFailed

        login(request, employee)
        response = {"username": username, "password": password}

        return JsonResponse(response, status=status.HTTP_201_CREATED)
