
from django import forms
from .models import CustomUser, Student

class CustomUserForm(forms.ModelForm):
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    class Meta:
        model = CustomUser
        fields = ['username','email', 'password', 'password2','first_name','last_name']
        widgets = {
            'password': forms.PasswordInput(),
        }
        labels = {
            'username': 'Username',
            'email': 'Email',
            'password': 'Password',
            'first_name': 'First Name',
            'last_name': 'Last Name',
        }
        required = {
            'username': True,
            'email': True,
            'password': True,
            'password2': True,
            'first_name': True,
            'last_name': True,
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")
        if password != password2:
            raise forms.ValidationError(
                "Passwords do not match"
            )

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['enrollment_no', 'course', 'institute']
        labels = {
            'enrollment_no': 'Enrollment Number',
            'course': 'Course',
            'institute': 'Institute/University',
        }
    

