from annoying.fields import AutoOneToOneField
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# Create your models here.


class UserProfile(models.Model):
    GENDER_CHOICES = (
        ("M", "Nam"),
        ("F", "Nữ"),
    )
    user = AutoOneToOneField(User, on_delete=models.CASCADE)
    cccd = models.CharField(
        max_length=12,
        validators=[
            RegexValidator(
                regex="^(?:[0-9]{9}|[0-9]{12})$",
                message="Phải nhập chính xác 9 hoặc 12 chữ số",
            ),
        ],
        blank=True,
        unique=True,
        verbose_name="CCCD"
    )
    address = models.CharField(max_length=150, blank=True, verbose_name="Địa chỉ")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, verbose_name="Giới tính")
    dob = models.DateField(blank=True, verbose_name="Ngày sinh")

    class Meta:
        verbose_name = "Hồ sơ người dùng"
        verbose_name_plural = "Các hồ sơ người dùng"