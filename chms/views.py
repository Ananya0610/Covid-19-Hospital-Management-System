from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from chms.models import Patient,Doctor,Appointment,Bed
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,FormView
from .forms import PatientCreateForm,DoctorCreateForm
from django.urls import reverse_lazy

def PatientCreate(request):
    context={}
    #form_class=PatientCreateForm
    #form = form_class(request.POST or None)
    if request.method == 'POST':
        form=PatientCreateForm(request.POST or None)
        if form.is_valid():
            patient=form.save()
            patient.save()
            #username=form.cleaned_data['username']
            #password=form.cleaned_data['password']
            #user=authenticate(username=username,password=password)
            messages.success(request, 'account created successfully')
            return redirect('login')
    else:
       form=PatientCreateForm()
    context['form']=form
    return render(request,"chms/register.html", context)

class PatientProfile(LoginRequiredMixin,TemplateView):
    pass
    #if patient.is_authenticated():
        #redirect_field_name = 'chms/patient_dashboard.html'

class DoctorListView(ListView):
    pass
    #model=Doctor
    #def get_queryset():
    #    return Doctor.objects.order_by('fname')

class DoctorCreate(CreateView):
    pass
    #model=Doctor
    #form = DoctorCreateForm
    #if request.method=='POST':
    #    form = DoctorCreateForm(request.POST)
    #    if form.is_valid():
    #        form.save(commit=True)
    #        redirect_field_name = 'chms/login.html'

class AppointmentCreate(LoginRequiredMixin,CreateView):
    pass
    #model=Appointment
    #form = AppointmentCreateForm
    #if request.method=='POST':
    #    form = AppointmentCreateForm(request.POST)
    #    if form.is_valid():
    #        form.save(commit=True)
    #        redirect_field_name = 'chms/appointment_details.html'

class BedCreate(LoginRequiredMixin,CreateView):
    pass
    #model=Bed
    #form=BedCreateForm
    #if request.method=='POST':
    #    form=BedCreateForm(request.POST)
    #    if form.is_valid():
    #        form.save(commit=True)
    #        redirect_field_name='chms/bed_detail.html'

class createInvoice():
    pass
