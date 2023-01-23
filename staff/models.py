from django.contrib.auth.models import AbstractUser
from django.db import models


class Employee(AbstractUser):
    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"

    class Position(models.IntegerChoices):
        director = 1, "Директор"
        administrator = 2, "Администратор"
        merchandiser = 3, "Мерчендайзер"
        analyst = 4, "Аналитик"

    position = models.PositiveSmallIntegerField(
        verbose_name="Должность",
        choices=Position.choices,
        default=Position.analyst
    )

    def __str__(self):
        return self.username
