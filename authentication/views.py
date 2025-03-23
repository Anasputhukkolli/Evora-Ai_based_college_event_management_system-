from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import UserProfile,EventPhoto,Sponsors,Event
from landing.models import ContactMessage
def admin_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        profile_picture = request.FILES.get('profile_picture')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered")
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()

            user_profile = UserProfile(user=user, profile_picture=profile_picture, role='admin')
            user_profile.save()

            messages.success(request, "Admin account created! Please log in.")
            return redirect('admin_login')

    return render(request, 'authentication/admin/index.html')


def student_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        profile_picture = request.FILES.get('profile_picture')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered")
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()

            user_profile = UserProfile(user=user, profile_picture=profile_picture, role='student')
            user_profile.save()

            messages.success(request, "Student account created! Please log in.")
            return redirect('student_login')

    return render(request, 'authentication/student/index.html')


def teacher_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        profile_picture = request.FILES.get('profile_picture')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered")
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()

            user_profile = UserProfile(user=user, profile_picture=profile_picture, role='teacher')
            user_profile.save()

            messages.success(request, "Teacher account created! Please log in.")
            return redirect('teacher_login')

    return render(request, 'authentication/teacher/index.html')
def event_head_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        profile_picture = request.FILES.get('profile_picture')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered")
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()

            user_profile = UserProfile(user=user, profile_picture=profile_picture, role='event_head')
            user_profile.save()

            messages.success(request, "event head account created! Please log in.")
            return redirect('event_head_login')

    return render(request, 'authentication/event_head/index.html')
def outsider_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        profile_picture = request.FILES.get('profile_picture')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered")
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()

            user_profile = UserProfile(user=user, profile_picture=profile_picture, role='others')
            user_profile.save()

            messages.success(request, " account created! Please log in.")
            return redirect('outsider_login')

    return render(request, 'authentication/outsider/index.html')
    

def admin_login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = User.objects.get(email=email)
            user = authenticate(request, username=user.username, password=password)
            
            if user is not None:
                user_profile = UserProfile.objects.get(user=user)

                if user_profile.role == 'admin':  # ✅ Only allow admins
                    login(request, user)
                    return redirect('admin_dashboard')
                else:
                    messages.error(request, "You are not authorized as an Admin!")
            else:
                messages.error(request, "Invalid credentials")
        except User.DoesNotExist:
            messages.error(request, "Invalid credentials")

    return render(request, 'authentication/admin/index.html')


def student_login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = User.objects.get(email=email)
            user = authenticate(request, username=user.username, password=password)
            
            if user is not None:
                user_profile = UserProfile.objects.get(user=user)

                if user_profile.role == 'student':  # ✅ Only allow students
                    login(request, user)
                    return redirect('student_dashboard')
                else:
                    messages.error(request, "You are not authorized as a Student!")
            else:
                messages.error(request, "Invalid credentials")
        except User.DoesNotExist:
            messages.error(request, "Invalid credentials")

    return render(request, 'authentication/student/index.html')


def teacher_login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = User.objects.get(email=email)
            user = authenticate(request, username=user.username, password=password)
            
            if user is not None:
                user_profile = UserProfile.objects.get(user=user)

                if user_profile.role == 'teacher':  # ✅ Only allow teachers
                    login(request, user)
                    return redirect('teacher_dashboard')
                else:
                    messages.error(request, "You are not authorized as a Teacher!")
            else:
                messages.error(request, "Invalid credentials")
        except User.DoesNotExist:
            messages.error(request, "Invalid credentials")

    return render(request, 'authentication/teacher/index.html')
def event_head_login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = User.objects.get(email=email)
            user = authenticate(request, username=user.username, password=password)
            
            if user is not None:
                user_profile = UserProfile.objects.get(user=user)

                if user_profile.role == 'event_head':  # ✅ Only allow event_heads
                    login(request, user)
                    return redirect('event_head_dashboard')
                else:
                    messages.error(request, "You are not authorized as a event_head!")
            else:
                messages.error(request, "Invalid credentials")
        except User.DoesNotExist:
            messages.error(request, "Invalid credentials")

    return render(request, 'authentication/eventhead/index.html')
def outsider_login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = User.objects.get(email=email)
            user = authenticate(request, username=user.username, password=password)
            
            if user is not None:
                user_profile = UserProfile.objects.get(user=user)

                if user_profile.role == 'others':  # ✅ Only allow teachers
                    login(request, user)
                    return redirect('outsider_dashboard')
                else:
                    messages.error(request, "You are not authorized as a others!")
            else:
                messages.error(request, "Invalid credentials")
        except User.DoesNotExist:
            messages.error(request, "Invalid credentials")

    return render(request, 'authentication/outsider/index.html')

from .models import Club

@login_required
def admin_dashboard(request):
    user_profile = UserProfile.objects.get(user=request.user)
    if user_profile.role != 'admin':
        messages.error(request, "Unauthorized access!")
        return redirect('home')  # Redirect unauthorized users
    
    # Fetch users by role
    teachers = UserProfile.objects.filter(role='teacher')
    students = UserProfile.objects.filter(role='student')
    admins = UserProfile.objects.filter(role='admin')
    event_heads = UserProfile.objects.filter(role='event_head')
    others = UserProfile.objects.filter(role='others')
    user = UserProfile.objects.all()
    if request.method == "POST":
        title = request.POST.get("title")
        category = request.POST.get("category")
        image = request.FILES.get("image")

        if title and category and image:
            EventPhoto.objects.create(title=title, category=category, image=image)
            return redirect("admin_dashboard")  # Redirect after successful upload

    categories = EventPhoto.EVENT_CATEGORIES  # Get categories from model
    if request.method == "POST":
        sponsor_name = request.POST.get("sponsor_name")
        sponsor_image = request.FILES.get("sponsor_image")

        if sponsor_name and sponsor_image:
            sponsor = Sponsors(title=sponsor_name, image=sponsor_image)
            sponsor.save()
            return redirect("admin_dashboard")  #
    contact =ContactMessage.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        date = request.POST.get('date')
        time = request.POST.get('time')
        category = request.POST.get('category')
        price = request.POST.get('price')
        venue = request.POST.get('venue')
        description = request.POST.get('description')
        poster = request.FILES.get('poster')  # Handling file uploads

        # Save to database
        Event.objects.create(
            name=name,
            date=date,
            time=time,
            category=category,
            venue=venue,
            poster=poster,
            description=description,
            price=price
        )
    events = Event.objects.all()
    club = Club.objects.all()
    bookedclub = ClubMembership.objects.all()
    aprrove = ApprovedMembership.objects.all()
    bookedevent = Booking.objects.all()

    return render(request, 'dashbord/admin_dashbord/index.html', {
        'teachers': teachers,
        'students': students,
        'admins': admins,
        'event_heads': event_heads,
        'others': others,
        "users": user,
        "categories": categories,
        "contact":contact,
        "events": events,
        "clubs":club,
        "bookedclub":bookedclub,
        "aprrove":aprrove,
        "bookedevent":bookedevent,
    })
    
from .forms import ClubForm

def create_club(request):
    if request.method == 'POST':
        form = ClubForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')  # Redirect to club listing
    else:
        form = ClubForm()
    return render(request, 'dashbord/admin_dashbord/create_club.html', {'form': form})
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import ClubMembership, ApprovedMembership

@login_required
def approve_membership(request, membership_id):
    membership = get_object_or_404(ClubMembership, id=membership_id)

    membership.role = 'Member'
    membership.save()

        # Store in the separate ApprovedMembership model
    ApprovedMembership.objects.create(user=membership.user, club=membership.club)

    messages.success(request, f'Membership for {membership.user.username} approved for the club {membership.club.name}!')

    return redirect(request.META.get('HTTP_REFERER', 'home'))  # Redirect back to the same page


def event_photos_list(request):
    photos = EventPhoto.objects.all()
    return render(request, "landing/index.html", {"photos": photos})



def delete_event(request, event_id):
    if request.method == "POST":
        event = get_object_or_404(Event, id=event_id)
        event.delete()
        return redirect('admin_dashboard')  # Redirect back to event listing page
 # Redirect back to event listing page


def delete_club(request, club_id):
    if request.method == "POST":
        club = get_object_or_404(Club, id=club_id)
        club.delete()
        messages.success(request, f"Club '{club.name}' has been deleted successfully.")
        return redirect('admin_dashboard')  # Redirect to the club list page

    # Fetch uploaded photos categorized
def delete_user(request, user_id):
    if not request.user.userprofile.role == 'admin':
        messages.error(request, "Unauthorized access!")
        return redirect('admin_dashboard')

    user = get_object_or_404(User, id=user_id)

    # Prevent admin from deleting themselves
    if request.user == user:
        messages.error(request, "You cannot delete yourself!")
        return redirect('admin_dashboard')

    user.delete()
    messages.success(request, "User deleted successfully.")
    return redirect('admin_dashboard')

from datetime import date

@login_required
def student_dashboard(request):
    user_profile = UserProfile.objects.get(user=request.user)
    if user_profile.role != 'student':
        messages.error(request, "Unauthorized access!")
        return redirect('home')  # Redirect unauthorized users
    events = Event.objects.all()
    categories = EventPhoto.EVENT_CATEGORIES 
    club = Club.objects.all()
    aprrove = ApprovedMembership.objects.all()
    bookedevent = Booking.objects.all()
    events_attended = Booking.objects.filter(user=request.user).count()
    upcoming_events = Event.objects.filter(date__gte=date.today()).count()
    club_memberships = ApprovedMembership.objects.filter(user=request.user).count()
    return render(request, 'dashbord/student_dashbord/index.html',{
        "events": events,
        "categories":categories,
        "clubs":club,
        "bookedclub":aprrove,
        "bookedevent":bookedevent,
        'events_attended': events_attended,
        'upcoming_events': upcoming_events,
        'club_memberships': club_memberships
    })




from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Club, ClubMembership

@login_required
def book_volunteer(request, club_id):
    club = get_object_or_404(Club, id=club_id)

    # Check if user is already a member
    if ClubMembership.objects.filter(user=request.user, club=club).exists():
        messages.warning(request, "You have already booked this club!")
    else:
        # Create membership
        ClubMembership.objects.create(user=request.user, club=club, role='Pending')
        messages.success(request, "Successfully booked for volunteering!")

    return redirect('student_dashboard')  # Redirect back to the student dashboard

@login_required
def teacher_dashboard(request):
    user_profile = UserProfile.objects.get(user=request.user)
    if user_profile.role != 'teacher':
        messages.error(request, "Unauthorized access!")
        return redirect('home')  # Redirect unauthorized users
    return render(request, 'dashbord/teacher_dashbord/index.html')
@login_required
def event_head_dashboard(request):
    user_profile = UserProfile.objects.get(user=request.user)
    categories = EventPhoto.EVENT_CATEGORIES  # Get categories from model

    if user_profile.role != 'event_head':
        messages.error(request, "Unauthorized access!")
        return redirect('home')  # Redirect unauthorized users
    if request.method == 'POST':
        name = request.POST.get('name')
        date = request.POST.get('date')
        time = request.POST.get('time')
        category = request.POST.get('category')
        venue = request.POST.get('venue')
        description = request.POST.get('description')
        poster = request.FILES.get('poster')  # Handling file uploads

        # Save to database
        Event.objects.create(
            name=name,
            date=date,
            time=time,
            category=category,
            venue=venue,
            poster=poster,
            description=description
        )
    events = Event.objects.all()
    club = Club.objects.all()
    bookedclub = ClubMembership.objects.all()
    aprrove = ApprovedMembership.objects.all()
    return render(request, 'dashbord/event_head_dashbord/index.html',{
    
        "events": events,
        "clubs":club,
        "bookedclub":bookedclub,
        "aprrove":aprrove,
        "categories":categories,
    })
@login_required
def outsider_dashboard(request):
    user_profile = UserProfile.objects.get(user=request.user)
    if user_profile.role != 'others':
        messages.error(request, "Unauthorized access!")
        return redirect('home')  # Redirect unauthorized users
    return render(request, 'dashbord/outsider_dashbord/index.html')


def logout_view(request):
    logout(request)
    return redirect('home')  # Redirect to the login page after logout



def adimin(request):
    return render(request, 'authentication/admin/index.html')
def others(request):
    return render(request, 'authentication/outsider/index.html')
def teacher(request):
    return render(request, 'authentication/teacher/index.html')
def event_head(request):
    return render(request, 'authentication/eventhead/index.html')
def student(request):
    return render(request, 'authentication/student/index.html')
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Event, Booking

@login_required
def book_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    
    # Check if the user has already booked the event
    if Booking.objects.filter(user=request.user, event=event).exists():
        return redirect('student_dashboard')  # Redirect to event page if already booked

    # Save the booking
    Booking.objects.create(user=request.user, event=event)

    return redirect('student_dashboard')  # Redirect after successful booking


