from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


# Create your models here.
class ReportCat(models.Model):
    name = models.CharField(max_length=255, verbose_name="Loại báo cáo")
    order = models.PositiveSmallIntegerField(unique=True, verbose_name="Thứ tự")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Loại báo cáo"
        verbose_name_plural = "Các loại báo cáo"


class Report(models.Model):
    reporter = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Người tạo"
    )
    cat = models.ForeignKey(
        ReportCat, on_delete=models.CASCADE, verbose_name="Danh mục"
    )
    create_date = models.DateField(auto_now_add=True, verbose_name="Ngày tạo")
    title = models.CharField(max_length=255, verbose_name="Tiêu đề")
    desc = models.TextField(blank=True, verbose_name="Mô tả")
    completed = models.BooleanField(default=False, verbose_name="Hoàn thành")
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveBigIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Báo cáo"
        verbose_name_plural = "Các Báo cáo"
