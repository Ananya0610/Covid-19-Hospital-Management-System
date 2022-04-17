from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from chms.models import Patient,Doctor,Appointment,Bed
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,FormView
from .forms import PatientCreateForm,DoctorCreateForm
from django.urls import reverse_lazy

from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()

class TestPage(TemplateView):
    template_name='chms/test.html'

def PatientCreate(request):
    context={}
    if request.method == 'POST':
        form=PatientCreateForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            username=form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request,username=username, password=password)
            user=User.objects.create_user(username=username,password=password)
            user.save()
            form.save()
            messages.success(request,'account created successfully')
            return redirect('login')
    else:
       form=PatientCreateForm()
    context['form']=form
    return render(request,"chms/register.html", context)

@login_required(login_url='patient_login')
def patient_dashboard(request):
    #pk=self.kwargs.get('pk')
    #patient=Patient.objects.get(pk)
    #doctor=models.Doctor.objects.get(user_id=request.user.id)
    return render(request,'chms/patient_dashboard.html')

class PatientUpdateView(LoginRequiredMixin,UpdateView):
    #login_url = '/login/dashboard/'
    redirect_field_name = '/patient_dashboard.html'
    form_class = PatientCreateForm
    model = Patient


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

@login_required(login_url='login')
def AppointmentCreate(request):
    patient=models.Patient.objects.get(user_id=request.user.id)
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.save()
            return HttpResponseRedirect('patient_appointment_detail')
            return redirect('chms:appointment_detail')
    else:
        form = AppointmentForm()
    return render(request, 'chms/appointment_create.html', {'form': form})

#class AppointmentCreate(LoginRequiredMixin,CreateView):
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
