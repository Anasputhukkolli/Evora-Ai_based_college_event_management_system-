from django.urls import path
from django.urls import path, include
from .views import adimin,others,teacher,event_head,student, admin_dashboard, logout_view,admin_register,admin_login_view,student_dashboard,student_register,student_login_view,teacher_register,teacher_login_view\
    ,teacher_dashboard,event_head_dashboard,event_head_login_view,event_head_register,outsider_dashboard,outsider_login_view,outsider_register,delete_user,delete_event\
,create_club,delete_club,book_volunteer,approve_membership,book_event

from . import views

urlpatterns = [
    path('adimin/', adimin, name='admin'),
    path('others/', others, name='others'),
    path('teacher/', teacher, name='teacher'),
    path('event_head/', event_head, name='event_head'),
    path('student/', student, name='student'),
    
    
    
    path('create_club/', create_club, name='create_club'),
    path('admin_dashboard/', admin_dashboard, name='admin_dashboard'),
    path('student_dashboard/', student_dashboard, name='student_dashboard'),
    path('teacher_dashboard/', teacher_dashboard, name='teacher_dashboard'),
    path('event_head_dashboard/', event_head_dashboard, name='event_head_dashboard'),
    path('outsider_dashboard/', outsider_dashboard, name='outsider_dashboard'),
    
    path('admin_register/', admin_register, name='admin_register'),
    path('admin_login/', admin_login_view, name='admin_login'),
    
    path('student_register/', student_register, name='student_register'),
    path('student_login/', student_login_view, name='student_login'),
    
    path('teacher_login/', teacher_login_view, name='teacher_login'),
    path('teacher_register/', teacher_register, name='teacher_register'),
    
    path('event_head_login/', event_head_login_view, name='event_head_login'),
    path('event_head_register/', event_head_register, name='event_head_register'),
    
    path('outsider_register/', outsider_register, name='outsider_register'),
    path('outsider_login/', outsider_login_view, name='outsider_login'),
    
    
    path('logout/', logout_view, name='logout'),
     
    path('delete-user/<int:user_id>/', delete_user, name='delete_user'),
    path('delete-event/<int:event_id>/', delete_event, name='delete_event'),
    path('delete-club/<int:club_id>/', delete_club, name='delete_club'),
    
    path('book-volunteer/<int:club_id>/', book_volunteer, name='book_volunteer'),
    path('approve/<int:membership_id>/', approve_membership, name='approve_membership'),
    path('book/<int:event_id>/', book_event, name='book_event'),      

    ]
