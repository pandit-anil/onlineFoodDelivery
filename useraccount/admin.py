from django.contrib import admin
from  django.contrib.auth.admin import UserAdmin
from . models import User

@admin.register(User)
class UserChange(UserAdmin):

        add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "username", "email", "mobile", "password1", "password2", "profile","address" , "is_staff",
                "is_active", "groups", "user_permissions"
            ),
        }),
            )
