from django.db import models
from django.contrib.auth.models import User


class License(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Tên bằng")
    tuition = models.PositiveIntegerField(default=1000, verbose_name="Học phí")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Loại bằng"
        verbose_name_plural = "Các loại bằng"


class DriverLicense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Học viên")
    create_date = models.DateField(auto_now_add=True, verbose_name="Ngày tạo")
    # Info
    license_fk = models.ForeignKey(
        License, on_delete=models.SET_NULL, null=True, verbose_name="Bằng"
    )
    course = models.ForeignKey(
        "Course",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Lớp đăng ký",
    )
    is_active = models.BooleanField(default=False, verbose_name="Kích hoạt")
    theory_ok = models.BooleanField(default=False, verbose_name="Hoàn thành lý thuyết")
    practice_ok = models.BooleanField(
        default=False, verbose_name="Hoàn thành thực hành"
    )
    is_qualified = models.BooleanField(default=False, verbose_name="Đã đạt")
    is_graduation = models.BooleanField(default=False, verbose_name="Đã tốt nghiệp")
    # Money info
    tuition = models.PositiveIntegerField(default=0, blank=True, verbose_name="Học phí")
    tuition_paid = models.PositiveIntegerField(
        default=0, blank=True, verbose_name="Học phí đã đóng"
    )
    exam_tuition = models.PositiveIntegerField(
        default=0, blank=True, verbose_name="Phí kiểm tra"
    )
    exam_tuition_paid = models.PositiveIntegerField(
        default=0, blank=True, verbose_name="Phí kiểm tra đã đóng"
    )
    exam_tuition_note = models.CharField(
        max_length=50, blank=True, verbose_name="Ghi chú phí kiểm tra"
    )
    a1_note = models.CharField(max_length=50, blank=True, verbose_name="Ghi chú A1")
    note = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username}-{self.license_fk.name}"

    def save(self, *args, **kwargs):
        # TODO: Check qualified
        super(DriverLicense, self).save(*args, **kwargs)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "license_fk"], name="unique_driver_license"
            )
        ]
        verbose_name = "Bằng lái xe"
        verbose_name_plural = "Bằng lái xe"
