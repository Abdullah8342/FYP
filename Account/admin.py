from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as CustomUserAdmin
from django.contrib.auth import get_user_model
# Register your models here.
User = get_user_model()

@admin.register(User)
class UserAdmin(CustomUserAdmin):
    model = User
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "first_name",
                    "last_name",
                    "roll",
                    "email",
                    "usable_password",
                    "password1",
                    "password2",
                ),
            },
        ),
    )
