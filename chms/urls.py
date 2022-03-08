from django.urls import path
from chms import views


app_name='chms'

urlpatterns=[
    path('about/',views.AboutView.as_view(),name='about'),
]
