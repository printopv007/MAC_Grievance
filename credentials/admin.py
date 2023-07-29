from django.contrib import admin
# Register your models here.
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

CustomUser = get_user_model()

# Custom form to use when editing users in the admin dashboard
class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser

# Custom form to use when adding users in the admin dashboard
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser

class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm

    # Customize the user list display as needed
    list_display = ['username', 'email', 'phone_number', 'department', 'is_staff', 'is_active']

# Register the custom user model with the admin site using the custom admin class
admin.site.register(CustomUser, CustomUserAdmin)
