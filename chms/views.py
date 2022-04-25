from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from chms.models import Patient,Doctor,Appointment,Bed
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,FormView
from django import forms
from chms.forms import PatientCreateForm,DoctorCreateForm,AppointmentCreateForm,BedCreateForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User

from django.contrib.auth import get_user_model
User = get_user_model()

class TestPageView(TemplateView):
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
def PatientDashboard(request):
    return render(request,'chms/patient_dashboard.html')

#@login_required(login_url='patient_login')
#def PatientUpdate(request,pk):
#    patient=get_object_or_404(Patient, pk=pk)
#    form=forms.PatientCreate(request.POST or None,instance=patient)
#    context={}
#    if form.is_valid():
#        form.save()
#        return HttpResponseRedirect("/"+pk)
#    context['form']=form
#    return render(request,'chms/patient_update.html',{'form':form,'patient':patient})

class PatientUpdateView(LoginRequiredMixin,UpdateView):
    login_url='/login/'
    model=Patient
    form_class=AppointmentCreateForm
    model=Appointment
    context_object_name='patient'
#    template_name='chms/patient_update.html'
#    def form_valid(self, form):
#        form.instance.patient= get_object_or_404(Patient, pk=self.kwargs.get('pk'))
#        return super(PatientUpdateView, self).form_valid(form)

class PatientList(LoginRequiredMixin,ListView):
    model = Patient
    def get_queryset(self):
        return Patinet.objects.order_by('fname')

class DoctorListView(ListView):
    pass

class DoctorCreate(CreateView):
    pass

@login_required
def AppointmentCreate(request):
    context={}
    #pk = self.kwargs.get('pk')
    patient = Patient.objects.filter().first()
    #patient = Patient.objects.all()
    form=AppointmentCreateForm()
    if request.method == 'POST':
        form = AppointmentCreateForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            appointment=Appointment.objects.create(patient=patient)
            form.save()
            appointment.save()
            messages.success(request,'appointment created')
            return redirect('chms:list_appointment')
    else:
        form = AppointmentCreateForm()
    context={'patient':patient,'form':form}
    return render(request,'chms/appointment_create.html',context)

class AppointmentList(LoginRequiredMixin,ListView):
    model=Appointment

class AppointmentListView(ListView):
    model =Appointment
    def get_queryset(self):
        return Appointment.objects.order_by('-app_date')

@login_required(login_url='login')
def BedCreate(request):
    context={}
    patient=Patient.objects.order_by("fname")
    if request.method == 'POST':
        form = BedCreateForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            bed=Bed.objects.create(patient=patient)
            message.success(request,'bed created')
            return redirect('chms:bed_detail')
    else:
        form = BedCreateForm()
    context={'patient':patient,'form':form}
    return render(request,'chms/bed_create.html',context)

class createInvoice():
    pass
