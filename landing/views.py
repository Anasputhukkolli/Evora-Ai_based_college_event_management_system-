from django.shortcuts import render,redirect
from .models import ContactMessage
from authentication.models import EventPhoto,Sponsors
from django.contrib import messages  # For success messages

def home(request):
    sports = EventPhoto.objects.filter(category='sports')
    arts = EventPhoto.objects.filter(category='arts')
    tech = EventPhoto.objects.filter(category='tech')
    cultural = EventPhoto.objects.filter(category='cultural')
    sponsors = Sponsors.objects.all()
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        if name and email and message:
            ContactMessage.objects.create(name=name, email=email, message=message)
            messages.success(request, "Your message has been sent successfully!")
            
    return render(request, "landing/index.html", {
        "sports": sports,
        "arts":arts,
        "tech":tech,
        "cultural": cultural,
        "sponsors":sponsors,
        
        })




