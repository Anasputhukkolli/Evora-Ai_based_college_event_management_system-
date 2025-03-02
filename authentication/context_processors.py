from .models import StudentProfile

def student_profile_processor(request):
    if request.user.is_authenticated:
        try:
            student_profile = StudentProfile.objects.get(email=request.user.email)
            return {'student_profile': student_profile}
        except StudentProfile.DoesNotExist:
            return {'student_profile': None}
    return {'student_profile': None}
