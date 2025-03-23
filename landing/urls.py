from django.urls import path
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('auth/', include('authentication.urls')),
    path("api/chatbot/", views.chatbot, name="chatbot"),
    path('api/generate-image/', views.generate_image, name='generate_image'),

]
