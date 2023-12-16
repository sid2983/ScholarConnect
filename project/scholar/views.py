from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
# from .models import *
from django.contrib import messages
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required

# # Create your views here.
# @login_required(login_url="/login")

# def scholarship_register(request):
#     return render(request, 'nss.html')

# def student_register(request):
#     data = request.POST
#     if request.method == "POST":
#         applicant_name = data.get('applicant_name')
#         phone_number = data.get('phone_number')
#         email = data.get('email')
#         password = data.get('password')
        
#         print(applicant_name)
#         user = student_regis.objects.filter(phone_number = phone_number)
#         print(user)
#         if user.exists():
#             messages.error(request, "Phone Number already taken!!!")
#             return redirect("register")
        
#         student_regis = student_regis.objects.create(
#             applicant_name = applicant_name, 
#             phone_number = phone_number, 
#             email = email)
        
#         student_regis.set_password(password)  
#         student_regis.save()
#         messages.info(request, "Account Created Successfully!!!")
        
#     return render(request, 'register.html')
    
# def login_page(request):
#     if request.method == "POST":
#         data = request.POST
#         phone_number = data.get('phone_number')
#         password = data.get('password')
        
#         if not student_regis.objects.filter(phone_number = phone_number).exists():
#             messages.info(request, "Invalid Phone_number!!")
#             return redirect('/login')
        
#         user = authenticate(phone_number = phone_number, password = password)
        
#         if user is not None:
#             print(phone_number)
#             print(password)
#             login(request, student_regis)
#             return redirect('/scholar_register')
            
#         else:
#             messages.error(request, 'Invalid Password!!')
#             return redirect('/login')
#     return render(request, 'login.html')
    

# def logout_page(request):
#     logout(request)
#     return redirect('/login')


def home(request):
    return render(request, 'base.html')


def dashboard(request):
    return render(request, 'users/dashboard.html')