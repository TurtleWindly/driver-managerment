from django.contrib import admin

from base.utils import vn_currency

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


@admin.register(License)
class LicenseAdmin(admin.ModelAdmin):
    list_display = ["name", "formated_tuition"]

    @admin.display(description="Học phí")
    def formated_tuition(self, obj):
        return vn_currency(obj.tuition)


@admin.register(DriverLicense)
class DriverLicenseAdmin(admin.ModelAdmin):
    pass


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    pass


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
