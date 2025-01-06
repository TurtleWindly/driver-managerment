from annoying.fields import AutoOneToOneField
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from phonenumber_field.modelfields import PhoneNumberField

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
    dob = models.DateField(blank=True, null=True, verbose_name="Ngày sinh")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, verbose_name="Giới tính")
    phone = PhoneNumberField(blank=True, verbose_name="SĐT")

    def __str__(self):
        return "Thông tin thêm"

    class Meta:
        verbose_name = "Hồ sơ người dùng"
        verbose_name_plural = "Các hồ sơ người dùng"