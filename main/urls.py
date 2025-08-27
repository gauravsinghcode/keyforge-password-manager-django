from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='app-home'),
    path("login/", auth_views.LoginView.as_view(template_name="main/login.html"), name="login"),
    path('register/', views.register, name="app-register"),
    path('dashboard/', views.dashboard, name='app-dashboard')
]