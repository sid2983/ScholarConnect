# from django.contrib.auth.base_user import BaseUserManager
# # from django.contrib.auth.models import UserManager   #  'Manager' object has no attribute 'get_by_natural_key'


# class CustomManager(BaseUserManager):
#     def create_user(self, phone_number, password = None, **extra_fields):
#         if not email:
#             raise ValueError("Email is required")

#         # extra_fields['email'] = self.normalize_email(extra_fields['email'])   # prabhat.patel@fc.com = PRABHAT.PATEL@FC.COM

#         email = self.normalize_email(email)

#         # creating Password
#         user = self.model(phone_number = phone_number, **extra_fields)
#         user.set_password(password)
#         user.save(using = self._db)

#         return user
    
#     def create_superuser(self, phone_number, password = None, **extra_fields):
#         extra_fields.setdefault('is_active',True)
#         extra_fields.setdefault('is_superuser',True)
#         extra_fields.setdefault('is_staff',True)

#         return self.create_user(phone_number , password, **extra_fields)
#     # 