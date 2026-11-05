
from django.conf import settings
from django.db import models


class Student(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="student_profile"
    )

    student_id = models.CharField(
        max_length=20,
        unique=True
    )

    department = models.CharField(max_length=100)

    level = models.PositiveIntegerField()

    lecturers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="assigned_students",
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student_id} - {self.user.username}"
