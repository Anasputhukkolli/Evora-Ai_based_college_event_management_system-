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


    



class EventPhoto(models.Model):
    EVENT_CATEGORIES = [
    ('sports', 'Mecasm'),
    ('arts', 'Arts'),
    ('tech', 'Tech'),
    ('cultural', 'Cultural'),
]
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='event_photos/')
    category = models.CharField(max_length=20, choices=EVENT_CATEGORIES)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.get_category_display()})"


class Sponsors(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='sponsors/')
    def __str__(self):
        return f"{self.title}"
    
    
from django.db import models

class Event(models.Model):
    EVENT_CATEGORIES = [
    ('sports', 'Mecasm'),
    ('arts', 'Arts'),
    ('tech', 'Tech'),
    ('cultural', 'Cultural'),
]
    name = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    venue = models.CharField(max_length=255)
    poster = models.ImageField(upload_to='event_posters/', blank=True, null=True)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=EVENT_CATEGORIES)
    price = models.CharField(max_length=255)


    def __str__(self):
        return self.name

from django.db import models

class Club(models.Model):
    name = models.CharField(max_length=255, unique=True)  # Club name
    description = models.TextField()  # Club description
    club_pic = models.ImageField(upload_to='club_pics/', blank=True, null=True)  # Club logo/image
    no_of_members = models.PositiveIntegerField(default=1)  # Number of members
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp
    created_by = models.CharField(max_length=255)  # Creator (could be linked to User model)
    contact_email = models.EmailField(blank=True, null=True)  # Club contact email
    status = models.CharField(
        max_length=10,
        choices=[('Active', 'Active'), ('Inactive', 'Inactive')],
        default='Active'
    )  # Club status

    def __str__(self):
        return self.name
from django.db import models
from django.contrib.auth.models import User



class ClubMembership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    club = models.ForeignKey(Club, on_delete=models.CASCADE)  
    role = models.CharField(
        max_length=20,
        choices=[('Member', 'Member'), ('Admin', 'Admin'), ('Pending', 'Pending')],
        default='Pending'
    )  
    joined_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return f"{self.user.username} - {self.club.name}"

# New Model to Store Approved Memberships
class ApprovedMembership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    approved_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} approved for {self.club.name}"

from django.db import models
from django.contrib.auth.models import User

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Assuming only logged-in users can book
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.event.name}"
