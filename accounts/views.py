from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy

from .forms import CustomAuthenticationForm


# Create your views here.
class LoginView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = "accounts/login.html"

    def form_valid(self, form: CustomAuthenticationForm):
        # Gọi phương thức đăng nhập của Django
        response = super().form_valid(form)

        remember_me = form.cleaned_data["remember_me"]
        # Nếu không lưu đăng nhập thì khi trình duyệt đóng sẽ logout
        if not remember_me:
            self.request.session.set_expiry(0)

        # Lấy tham số 'next' từ URL
        next_url = self.request.POST.get("next")
        if next_url:
            return redirect(next_url)  # Chuyển hướng đến 'next'
        else:
            # Nếu không có 'next', chuyển đến trang mặc định
            return response

    def get_success_url(self) -> str:
        return reverse_lazy("home:home")

