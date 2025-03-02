from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('event_head', 'Event Head'),
        ('others', 'Others'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='student')

    def __str__(self):
        return f"{self.user.username} - {self.role}"

class StudentProfile(models.Model):
    username = models.CharField(max_length=155)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=155)  # We will store hashed passwords
    profile_picture = models.ImageField(upload_to='profile_pics/', default='default.jpg')

    
    def __str__(self):
        return self.username