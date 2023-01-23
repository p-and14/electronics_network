from django.contrib.auth import password_validation
from rest_framework import serializers

from staff.models import Employee


class EmployeeRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[password_validation.validate_password])

    class Meta:
        model = Employee
        fields = ["id", "username", "password", "first_name", "last_name", "email", "position"]


    def create(self, validated_data):
        password = self.initial_data.get("password")
        user = Employee.objects.create(**validated_data)

        user.set_password(password)
        user.save()
        return user
