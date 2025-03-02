from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import UserProfile

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


@login_required
def admin_dashboard(request):
    user_profile = UserProfile.objects.get(user=request.user)
    if user_profile.role != 'admin':
        messages.error(request, "Unauthorized access!")
        return redirect('home')  # Redirect unauthorized users
    return render(request, 'dashbord/admin_dashbord/index.html')


@login_required
def student_dashboard(request):
    user_profile = UserProfile.objects.get(user=request.user)
    if user_profile.role != 'student':
        messages.error(request, "Unauthorized access!")
        return redirect('home')  # Redirect unauthorized users
    return render(request, 'dashbord/student_dashbord/index.html')


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
    if user_profile.role != 'event_head':
        messages.error(request, "Unauthorized access!")
        return redirect('home')  # Redirect unauthorized users
    return render(request, 'dashbord/event_head_dashbord/index.html')
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

