from django.contrib import admin

from .models import Report, ReportCat

# Register your models here.


@admin.register(ReportCat)
class ReportCatAdmin(admin.ModelAdmin):
    list_display = ["order", "name"]
    ordering = ["order"]


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = [
        "username",
        "category",
        "create_date",
        "title",
        "completed",
    ]
    ordering = ["create_date", "completed"]

    @admin.display(description="User")
    def username(self, obj):
        return obj.reporter.username

    @admin.display(description="loại")
    def category(self, obj):
        return obj.cat.name
