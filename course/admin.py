from django.contrib import admin

from base.utils import vn_currency


from .forms import CourseForm, DriverLicenseForm
from .models import (
    License,
    DriverLicense,
    Course,
    Lesson,
    LessonAttend,
    PracticeAttend,
    CourseTemplate,
    LessonTemplate,
)

# Register your models here.


class LessonAttendInline(admin.TabularInline):
    model = LessonAttend
    extra = 1


class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 1
    show_change_link = True


@admin.register(License)
class LicenseAdmin(admin.ModelAdmin):
    list_display = ["name", "formated_tuition"]

    @admin.display(description="Học phí")
    def formated_tuition(self, obj):
        return vn_currency(obj.tuition)


@admin.register(DriverLicense)
class DriverLicenseAdmin(admin.ModelAdmin):
    form = DriverLicenseForm
    list_display = [
        "user",
        "create_date",
        "license_fk",
        "is_active",
        "is_qualified",
        "is_graduation",
    ]
    list_filter = ["create_date", "license_fk", "is_active"]
    search_fields = ["user__username"]


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    form = CourseForm
    inlines = [
        LessonInline,
    ]


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    inlines = [
        LessonAttendInline,
    ]


@admin.register(LessonAttend)
class LessonAttendAdmin(admin.ModelAdmin):
    pass


@admin.register(PracticeAttend)
class PracticeAttendAdmin(admin.ModelAdmin):
    pass


@admin.register(CourseTemplate)
class CourseTemplateAdmin(admin.ModelAdmin):
    pass


@admin.register(LessonTemplate)
class LessonTemplateAdmin(admin.ModelAdmin):
    pass
