from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import models
from django.contrib import auth
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView

# Create your views here.
from django.shortcuts import render
from django.urls import reverse_lazy
from . import forms

class SignUp(CreateView):
    form_class=forms.PatientCreateForm
    success_url=reverse_lazy("login")
    template_name="login.html"

class PatientUpdate(UpdateView):
    pass
