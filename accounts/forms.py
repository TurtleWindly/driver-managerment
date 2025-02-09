from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, Row, Column, Field
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.core.validators import RegexValidator
from django.utils.translation import gettext as _
from phonenumber_field.formfields import PhoneNumberField

from course.models import License


class CustomAuthenticationForm(AuthenticationForm):
    remember_me = forms.BooleanField(
        initial=False, required=False, label="Lưu đăng nhập"
    )


class StudentCreateAccountForm(forms.Form):
    GENDER_CHOICES = (
        ("M", "Nam"),
        ("F", "Nữ"),
    )
    cccd = forms.CharField(
        max_length=12,
        validators=[
            RegexValidator(
                regex="^(?:[0-9]{9}|[0-9]{12})$",
                message="Phải nhập chính xác 9 hoặc 12 chữ số",
            ),
        ],
        label="CCCD",
    )
    last_name = forms.CharField(max_length=50, label="Họ lót")
    first_name = forms.CharField(max_length=50, label="Tên")
    phone = PhoneNumberField(label=_("SĐT"))
    phone.error_messages["invalid"] = "Số điện thoại nhập sai"
    email = forms.EmailField(label="email")
    dob = forms.DateField(label="Ngày sinh")
    gender = forms.ChoiceField(
        label="Giới tính", choices=GENDER_CHOICES, widget=forms.RadioSelect
    )
    password = forms.CharField(widget=forms.PasswordInput, label="Mật khẩu")
    license_fk = forms.ModelChoiceField(
        queryset=License.objects.all().order_by("name"), label="Chọn bằng lái"
    )
