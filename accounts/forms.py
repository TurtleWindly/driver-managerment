from django import forms
from django.contrib.auth.forms import AuthenticationForm


class CustomAuthenticationForm(AuthenticationForm):
    remember_me = forms.BooleanField(initial=False, required=False, label="Lưu đăng nhập")
