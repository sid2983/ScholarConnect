# users/urls.py

from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('register/', views.register_student, name='register_student'), 
    path('registration_success/', views.registration_success, name='registration_success'), 
    path('studentLogin/', views.student_login, name='student_login'),       
    path('studentLogout/', views.student_logout, name='student_logout'),
    # path('profile/', views.profile, name='profile'),
]