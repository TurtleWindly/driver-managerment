from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

from .models import UserProfile

# Register your models here.
admin.site.unregister(User)


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = "Hồ sơ người dùng"
    fk_name = "user"


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    inlines = [UserProfileInline]
