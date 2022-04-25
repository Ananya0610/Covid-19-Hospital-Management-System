from django.urls import path

from . import views
from django.contrib.auth import views as auth_views

app_name='chms'

urlpatterns=[
    path("login/",auth_views.LoginView.as_view(template_name="chms/login.html"),name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="chms/thanks.html"), name="logout"),
    path("register/",views.PatientCreate,name='register'),
    path("dashboard/",views.PatientDashboard,name='patient_dashboard'),
    path("dashbaord/<pk>/update",views.PatientUpdateView.as_view(),name='patient_update'),
    #path("test/",views.TestPageView.as_view(),name="test"),
    path("create/appointment/",views.AppointmentCreate,name="create_appointment"),
    path("",views.AppointmentList.as_view(),name="list_appointment"),
    #path('',views.AppointmentListView.as_view(),name='appointment_list'),
    #path("update/appointment/",views.AppointmentUpdate,name="update_appointment"),
    #path("delete/appointment/",views.AppointmentDelete,name="delete_appointment"),
    path("create/bed/",views.BedCreate,name="create_bed"),
]
