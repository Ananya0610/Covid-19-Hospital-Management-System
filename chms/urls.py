from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name='chms'

urlpatterns=[
    path("chms/login/",auth_views.LoginView.as_view(template_name="chms/login.html"),name='login'),
    path("logout/", auth_views.LogoutView.as_view(template_name="chms/thanks.html"), name="logout"),
    path("register/",views.PatientCreate,name='register'),
]
