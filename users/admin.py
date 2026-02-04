from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User

    list_display = (
        "id",
        "username",
        "email",
        "role",
        "is_suspended",
        "is_staff",
    )

    list_filter = ("role", "is_suspended", "is_staff")

    fieldsets = UserAdmin.fieldsets + (
        ("Role Info", {"fields": ("role", "is_suspended")}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Role Info", {"fields": ("role", "is_suspended")}),
    )
