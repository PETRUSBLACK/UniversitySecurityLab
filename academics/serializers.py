
from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):

    username = serializers.CharField(
        source="user.username",
        read_only=True
    )

    class Meta:
        model = Student
        fields = [
            "id",
            "student_id",
            "username",
            "department",
            "level",
        ]
        read_only_fields = ["id", "student_id", "username"]
