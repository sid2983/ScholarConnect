
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, logout
from .forms import CustomUserForm, StudentForm
from django.http import HttpResponseRedirect

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
# Create your views here.


def register_student(request):
    if request.method == 'POST':
        user_form = CustomUserForm(request.POST)
        student_form = StudentForm(request.POST)

        # Check if both forms are valid
        if user_form.is_valid() and student_form.is_valid():
            # Save the user form with user_type set to 1 for students
            user = user_form.save(commit=False)
            user.user_type = 1  # Assuming 1 represents the "Student" user type
            user.save()

            # Save the student form with the user instance
            student = student_form.save(commit=False)
            student.user = user
            student.save()

            return HttpResponseRedirect(reverse("users:registration_success"))

    else:
        user_form = CustomUserForm()
        student_form = StudentForm()

    return render(request, 'users/register.html', {'user_form': user_form, 'student_form': student_form})


def registration_success(request):
    print('it worked')
    print(request.user)
    return render(request, 'users/registration_success.html')






# def student_login(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             print('working')
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(request, username=username, password=password)
#             print('working')
#             if user is not None:
#                 login(request, user)
#                 print('login working')

#                 # Redirect based on user type
#                 if hasattr(user, 'student'):
#                     print('student')
#                     return HttpResponseRedirect(reverse('scholar:dashboard'))

#                 elif hasattr(user, 'institute'):
#                     print('institute')
#                     HttpResponseRedirect(reverse('scholar:dashboard'))

#                 elif hasattr(user, 'stateauthority'):
#                     print('stateauthority')
#                     HttpResponseRedirect(reverse('scholar:dashboard'))
#                 else:
#                     messages.error(request, 'Unknown user type.')
#                     HttpResponseRedirect(reverse('scholar:dashboard'))



#             else:
#                 messages.error(request, 'Invalid username or password.')

#     else:
#         form = AuthenticationForm()

#     return render(request, 'users/login.html', {'form': form})
def student_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        print(form.errors)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                if user.user_type == 1:  # Check if user_type is 1 (Student)
                    login(request, user)
                    return HttpResponseRedirect(reverse('scholar:dashboard'))
                else:
                    messages.error(request, 'Invalid user type for student login.')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            print(form.errors)
            messages.error(request, f'Form is not valid. Check form data: {form.errors}')

    else:
        form = AuthenticationForm()

    return render(request, 'users/login.html', {'form': form})



def student_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('users:student_login'))