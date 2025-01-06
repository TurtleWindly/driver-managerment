from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation

from reporter.models import Report

from .license_models import DriverLicense, License


class Course(models.Model):
    name = models.CharField(max_length=255, verbose_name="Tên khóa học")
    teachers = models.ManyToManyField(
        User, related_name="teaching_courses", blank=True, verbose_name="Giáo viên"
    )
    students = models.ManyToManyField(
        DriverLicense, related_name="enrolled_courses", blank=True, verbose_name="Học viên"
    )
    exam_date = models.DateField(blank=True, verbose_name="Ngày thi")
    graduation_date = models.DateField(blank=True, verbose_name="Ngày tốt nghiệp")
    license_fk = models.ForeignKey(License, on_delete=models.SET_NULL, null=True, verbose_name="Loại bằng")
    reports = GenericRelation(Report)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Khóa học"
        verbose_name_plural = "Các khóa học"


class Lesson(models.Model):
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, verbose_name="Khóa học"
    )
    name = models.CharField(max_length=255, verbose_name="Tên bài học")
    start = models.DateTimeField(blank=True, null=True, verbose_name="Bắt đầu")
    end = models.DateTimeField(blank=True, null=True, verbose_name="Kết thúc")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Bài học"
        verbose_name_plural = "Các bài học"


class LessonAttend(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name="Bài học")
    student = models.ForeignKey(DriverLicense, on_delete=models.CASCADE, verbose_name="Học viên")
    present = models.BooleanField(default=False, verbose_name="Hiện diện")

    class Meta:
        verbose_name = "Điểm danh lý thuyết"
        verbose_name_plural = "Điểm danh lý thuyết"


class PracticeAttend(models.Model):
    student = models.ForeignKey(DriverLicense, on_delete=models.CASCADE, verbose_name="Học viên")
    time = models.PositiveSmallIntegerField(default=1, verbose_name="Thời gian")
    date = models.DateField(auto_now_add=True, verbose_name="Ngày")

    class Meta:
        verbose_name = "Điểm danh thực hành"
        verbose_name_plural = "Điểm danh thực hành"
