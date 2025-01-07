from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

from course.models import DriverLicense, Course

from course.forms import DriverLicenseForm

from .models import UserProfile

# Register your models here.
admin.site.unregister(User)


class TeachingCourseInline(admin.TabularInline):
    model = Course.teachers.through
    extra = 1
    verbose_name = "Lớp dạy"
    verbose_name_plural = "Các lớp giảng dạy"


class DriverLicenseInline(admin.StackedInline):
    model = DriverLicense
    form = DriverLicenseForm
    extra = 1
    show_change_link = True


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = "Hồ sơ người dùng"
    fk_name = "user"


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    inlines = [UserProfileInline, TeachingCourseInline, DriverLicenseInline]
