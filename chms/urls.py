from django.urls import path
from . import views

app_name='chms'

urlpatterns=[
    path("login/", auth_views.LoginView.as_view(template_name="chms/login.html"),name='login'),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path('patient/', views.CreatePatient.as_view(), name='user_login'),
]
