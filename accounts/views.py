from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.shortcuts import redirect, render, HttpResponseRedirect
from django.urls import reverse_lazy

from course.models import DriverLicense

from .models import UserProfile
from .forms import CustomAuthenticationForm, StudentCreateAccountForm


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


def student_create_account(request, *args, **kwargs):
    if request.method == "POST":
        form = StudentCreateAccountForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create(
                username=form.cleaned_data["cccd"],
                password=form.cleaned_data["password"],
                email=form.cleaned_data["email"],
                last_name=form.cleaned_data["last_name"],
                first_name=form.cleaned_data["first_name"],
            )
            UserProfile.objects.create(
                user=new_user,
                cccd=form.cleaned_data["cccd"],
                dob=form.cleaned_data["dob"],
                gender=form.cleaned_data["gender"],
                phone=form.cleaned_data["phone"],
            )
            DriverLicense.objects.create(
                user=new_user, license_fk=form.cleaned_data["license_fk"]
            )
            return HttpResponseRedirect(reverse_lazy("home:home"))
    else:
        form = StudentCreateAccountForm()
    return render(request, "accounts/signup.html", {"form": form})
