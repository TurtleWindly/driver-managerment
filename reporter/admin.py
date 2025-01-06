from django.contrib import admin

from .models import Report, ReportCat

# Register your models here.


@admin.register(ReportCat)
class ReportCatAdmin(admin.ModelAdmin):
    pass


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    pass
