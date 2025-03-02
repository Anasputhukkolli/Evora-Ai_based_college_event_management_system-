from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from .models import StudentProfile  # Import StudentProfile

class StudentAuthBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            student = StudentProfile.objects.get(email=email)
            if check_password(password, student.password):  # Validate password
                return student
        except StudentProfile.DoesNotExist:
            return None
        return None

    def get_user(self, student_id):
        try:
            return StudentProfile.objects.get(pk=student_id)
        except StudentProfile.DoesNotExist:
            return None
