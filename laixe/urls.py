"""
URL configuration for laixe project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from annoying.functions import get_config
from django.contrib import admin
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    path("", include("home.urls")),
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("course/", include("course.urls")),
    path("report/", include("reporter.urls")),
] + debug_toolbar_urls()

if get_config("DEBUG"):
    urlpatterns.append(path("__reload__/", include("django_browser_reload.urls")))
