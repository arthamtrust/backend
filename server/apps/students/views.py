from rest_framework import viewsets

from apps.students.models import Student
from apps.students.serializers import StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer
