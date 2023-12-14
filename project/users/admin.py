# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from .models import CustomUser, Student, Institute, StateAuthority

# class StudentAdmin(admin.ModelAdmin):
#     list_display = [field.name for field in Student._meta.fields]

# class InstituteAdmin(admin.ModelAdmin):
#     list_display = [field.name for field in Institute._meta.fields]
    
#     def save_model(self, request, obj, form, change):
#         # Save the Institute instance
#         super().save_model(request, obj, form, change)

#         # Check if the user is already assigned
#         if not obj.user:
#             # Assign the current user to the Institute's user field
#             obj.user = request.user
#             obj.save()

# class StateAuthorityAdmin(admin.ModelAdmin):
#     list_display = [field.name for field in StateAuthority._meta.fields]

#     def save_model(self, request, obj, form, change):
#         # Automatically create a user if it doesn't exist
#         if not obj.user:
#             user = CustomUser.objects.create_user(username=obj.state_code)
#             obj.user = user
#             obj.save()  # Save the StateAuthority instance first
#         else:
#             obj.save()  # Save the StateAuthority instance with the existing user

# # Register CustomUser with the BaseUserAdmin
# admin.site.register(CustomUser, BaseUserAdmin)
# admin.site.register(Student, StudentAdmin)
# admin.site.register(Institute, InstituteAdmin)
# admin.site.register(StateAuthority, StateAuthorityAdmin)



from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser, Student, Institute, StateAuthority

class StudentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Student._meta.fields]

class StudentInline(admin.StackedInline):  # or admin.TabularInline
    model = Student

class InstituteAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Institute._meta.fields]
    
    def save_model(self, request, obj, form, change):
        # Save the Institute instance
        super().save_model(request, obj, form, change)

        # Check if the user is already assigned
        if not obj.user:
            # Assign the current user to the Institute's user field
            user = CustomUser.objects.create_user(username=obj.institute_code, user_type=2)  # Set user_type to Institute (2)
            obj.user = user
            obj.save()

class StateAuthorityAdmin(admin.ModelAdmin):
    list_display = [field.name for field in StateAuthority._meta.fields]

    def save_model(self, request, obj, form, change):
        # Save the StateAuthority instance
        super().save_model(request, obj, form, change)

        # Check if the user is already assigned
        if not obj.user:
            # Assign the current user to the StateAuthority's user field
            user = CustomUser.objects.create_user(username=obj.state_code, user_type=3)  # Set user_type to StateAuthority (3)
            obj.user = user
            obj.save()

# Register CustomUser with the BaseUserAdmin
admin.site.register(CustomUser, BaseUserAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Institute, InstituteAdmin)
admin.site.register(StateAuthority, StateAuthorityAdmin)
