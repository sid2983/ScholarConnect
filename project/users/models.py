# from django.db import models

# # Create your models here.
# from django.db import models
# from django.contrib.auth.models import AbstractUser
# # Create your models here.

# class UserInfo(models.Model):
    
#     ##  -----General-Information----
#     domicile = models.CharField(max_length=50)
#     scholar_cat = models.CharField(max_length=50)
#     name = models.CharField(max_length=50)
#     dob = models.DateField(auto_now=False, auto_now_add=False)
#     gender = models.CharField(max_length=50)
#     religion = models.CharField(max_length=50)
#     category = models.CharField(max_length=50)
#     father_name = models.CharField(max_length=50)
#     mother_name = models.CharField(max_length=50)
#     annual_income = models.IntegerField()
#     phone_number = models.CharField(max_length=10,unique=True, null=True)
#     email = models.EmailField(max_length=254)
    
    
#     ##   ----Academic Details----
#     # current
#     enrollment_no = models.IntegerField()
#     admission_year = models.DateField(auto_now=False, auto_now_add=False)
#     course = models.CharField(max_length=50)
    
#     # Previous 12th Detail
#     roll_12 = models.IntegerField()
#     board_name_12 = models.CharField(max_length=50)
#     marks_12 = models.IntegerField()
    
#     # Previous 10th Detail
#     roll_10 = models.IntegerField()
#     board_name_10 = models.CharField(max_length=50)
#     marks_10 = models.IntegerField()

#     ##  -- Other Details --
#     disabled = models.CharField(max_length=50)
#     marital_status = models.CharField(max_length=50)
#     parents_profession = models.CharField(max_length=50)
    

# class student_regis(AbstractUser):
#     applicant_name = models.CharField(max_length=150) 
#     phone_number = models.IntegerField(unique=True)
#     email = models.EmailField(max_length=254,unique=True)
#     password = models.CharField(max_length=20)
#     user_profile_image = models.ImageField(upload_to="profile")

#     USERNAME_FIELD = 'phone_number'
#     REQUIRED_FIELDS = []



# class User(AbstractUser):
#     phone_number = models.CharField(unique = True, max_length=50)
#     is_phone_verified = models.BooleanField(default = False)
#     otp = models.CharField(max_length=6)

#     USERNAME_FIELD = 'phone_number'
#     REQUIRED_FIELDS = []
#     objects = UserManager()

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     mobile = models.CharField(max_length=20)
#     otp = models.CharField(max_length=6)
#     password = models.CharField(max_length=50)



from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager,Group

class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, user_type=None, **extra_fields):
        user = self.model(username=username, user_type=user_type, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('user_type', 4)
        return self.create_user(username, password, **extra_fields)

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'Student'),
        (2, 'Institute'),
        (3, 'StateAuthority'),
        (4, 'superuser')
    )

    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, null=True)
    objects = CustomUserManager()

    def save(self, *args, **kwargs):
        # Set any additional behavior before saving the user
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.username} - {self.get_user_type_display()}"


class StateAuthority(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    
    ##  -----State Authority Information----
    state_name = models.CharField(max_length=255)
    state_code = models.CharField(max_length=20, unique=True)
    # Add any other relevant fields specific to the state authority

    def __str__(self):
        return self.state_name



class Institute(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    
    ##  -----Institute Information----
    institute_name = models.CharField(max_length=255)
    institute_code = models.CharField(max_length=20, unique=True)
    # Add any other relevant fields specific to the institute

    def __str__(self):
        return self.institute_name
    

class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    
    ##  -----General Information----
    domicile = models.CharField(max_length=255)
    scholar_cat = models.CharField(max_length=255)
    dob = models.DateField(default='2000-01-01')
    gender = models.CharField(max_length=10)
    religion = models.CharField(max_length=255)
    category_caste = models.CharField(max_length=255)
    father_name = models.CharField(max_length=255)
    mother_name = models.CharField(max_length=255)
    annual_income = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)
    phone_number = models.CharField(max_length=15,unique=True, null=True)

    ##   ----Academic Details----
    # current
    institute = models.ForeignKey(Institute, on_delete=models.SET_NULL, null=True, blank=True)
    enrollment_no = models.CharField(max_length=20)
    admission_year = models.IntegerField(null=True, blank=True)
    course = models.CharField(max_length=255,null=True, blank=True)
    
    # Previous 12th Detail
    roll_12 = models.CharField(max_length=20)
    board_name_12 = models.CharField(max_length=255,null=True, blank=True)
    marks_12 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    
    # Previous 10th Detail
    roll_10 = models.CharField(max_length=20, null=True, blank=True)
    board_name_10 = models.CharField(max_length=255, null=True, blank=True)
    marks_10 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    ##  -- Other Details --
    disabled = models.BooleanField(default=False)
    marital_status = models.CharField(max_length=20, null=True, blank=True)
    parents_profession = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.user.username  # Assuming 'username' is a field in AbstractUser





# Create groups during the initial migration
def create_groups(sender, **kwargs):
    Group.objects.get_or_create(name='Student')
    Group.objects.get_or_create(name='Institute')
    Group.objects.get_or_create(name='StateAuthority')


# Connect the create_groups function to the post_migrate signal
models.signals.post_migrate.connect(create_groups, sender=models)

# Disconnect the create_groups function after the initial migration
models.signals.post_migrate.disconnect(create_groups, sender=models)

