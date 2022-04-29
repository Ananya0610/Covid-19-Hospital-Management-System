from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name='chms'

urlpatterns=[
    path("login/",auth_views.LoginView.as_view(template_name="chms/login.html"),name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="chms/thanks.html"), name="logout"),
    path("register/patient/",views.PatientCreate,name='register_patient'),
    path("dashboard/patient/",views.PatientDashboard,name='patient_dashboard'),
    path("dashboard/update/<str:username>/",views.PatientUpdateView,name='patient_update'),
    path('dashboard/<int:pk>/detail',views.PatientDetailView.as_view(),name='patient_detail'),
    #path("test/",views.TestPageView.as_view(),name="test"),

    path("create/appointment/<str:username>/",views.AppointmentCreate,name="create_appointment"),
    path("list/appointment/<str:username>/",views.AppointmentListView,name="list_appointment"),
    #path('',views.AppointmentListView.as_view(),name='appointment_list'),
    #path("update/appointment/",views.AppointmentUpdate,name="update_appointment"),
    path("delete/appointment/<int:pk>",views.AppointmentDeleteView,name="delete_appointment"),

    path("create/bed/<str:username>/",views.BedCreate,name="create_bed"),
    path("list/bed/<str:username>/",views.BedListView,name="list_bed"),
    #path("update/appointment/",views.AppointmentUpdate,name="update_appointment"),
    path("delete/bed/<int:pk>/",views.BedDeleteView,name="delete_bed"),

    path("register/doctor/",views.DoctorCreate,name='register_doctor'),
    path("dashboard/doctor/",views.DoctorDashboard,name='doctor_dashboard'),
]
