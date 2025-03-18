from django.contrib import admin
from .models import UserProfile,EventPhoto,Sponsors,Event,Club,ClubMembership,ApprovedMembership,Booking# Import your model

# Register the model
admin.site.register(UserProfile) 
admin.site.register(EventPhoto) 
admin.site.register(Sponsors) 
admin.site.register(Event) 
admin.site.register(Club) 
admin.site.register(ClubMembership) 
admin.site.register(ApprovedMembership) 
admin.site.register(Booking) 
# admin.site.register(StudentProfile)
