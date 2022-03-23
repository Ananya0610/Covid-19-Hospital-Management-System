from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from chms.models import Patient,Doctor,Appointment,Bed
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView
from chms.forms import PatientCreateForm
from django.urls import reverse_lazy

class PatientCreate(CreateView):
    form=PatientCreateForm()

    if request.method == 'POST':
        form=PatientCreateForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            redirect_field_name = 'chms/login.html'
        else:
            form=PatientCreateForm()

class PatientProfile(LoginRequiredMixin,TemplateView):
    if patient.is_authenticated():
        redirect_field_name = 'chms/patient_dashboard.html'

class DoctorListView(ListView):
    model=Doctor
    def get_queryset():
        return Doctor.objects.order_by('fname')

class DoctorCreate(CreateView):
    model=Doctor
    form = DoctorCreateForm
    if request.method=='POST':
        form = DoctorCreateForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            redirect_field_name = 'chms/login.html'

class AppointmentCreate(LoginRequiredMixin,CreateView):
    model=Appointment
    form = AppointmentCreateForm
    if request.method=='POST':
        form = AppointmentCreateForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            redirect_field_name = 'chms/appointment_details.html'

class BedCreate(LoginRequiredMixin,CreateView):
    model=Bed
    form=BedCreateForm
    if request.method=='POST':
        form=BedCreateForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            redirect_field_name='chms/bed_detail.html'

class createInvoice():
    pass
