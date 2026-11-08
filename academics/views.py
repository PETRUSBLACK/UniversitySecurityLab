
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Student
from .serializers import StudentSerializer


class StudentViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.role == "STUDENT":
            return Student.objects.filter(user=user)

        if user.role == "LECTURER":
            return Student.objects.filter(lecturers=user)

        if user.role == "ADMIN":
            return Student.objects.all()

        return Student.objects.none()
