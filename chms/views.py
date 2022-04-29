from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
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
    return render(request,"chms/patient_register.html", context)

@login_required(login_url='login')
def PatientDashboard(request):
    return render(request,'chms/patient_dashboard.html')

@login_required(login_url='patient_login')
def PatientUpdateView(request,username):
    patient=get_object_or_404(Patient,username=username)
    form=PatientCreateForm(request.POST or None,instance=patient)
    context={}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return redirect("chms:patient_dashboard")
    return render(request,'chms/patient_update.html',{'form':form})

class PatientDetailView(LoginRequiredMixin,DetailView):
    model=Patient

class PatientList(LoginRequiredMixin,ListView):
    pass

class DoctorListView(ListView):
    pass

def DoctorCreate(request):
    context={}
    if request.method == 'POST':
        form=DoctorCreateForm(request.POST)
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
       form=DoctorCreateForm()
    context['form']=form
    return render(request,"chms/doctor_register.html", context)

@login_required(login_url='login')
def DoctorDashboard(request):
    return render(request,'chms/doctor_dashboard.html')

@login_required
def AppointmentCreate(request,username):
    context={}
    patient = Patient.objects.filter(username__iexact=username).first()
    if request.method == 'POST':
        form = AppointmentCreateForm(request.POST,instance=patient)
        if form.is_valid():
            form.save(commit=False)
            appointment=authenticate(request)
            appointment=Appointment.objects.create(patient=patient)
            appointment.save()
            form.save()
            messages.success(request,'appointment created')
            return redirect('chms:list_appointment',username=username)
    else:
        form = AppointmentCreateForm()
    context['form']=form
    return render(request,'chms/appointment_create.html',context)

def AppointmentListView(request,username):
    context={}
    patient = Patient.objects.filter(username__iexact=username)
    appointment=Appointment.objects.all()
    context['appointment']=appointment
    return render(request,'chms/appointment_list.html',context)

def AppointmentDeleteView(request,pk):
    appointment=Appointment.objects.get(pk=pk)
    appointment.delete()
    return redirect("chms:list_appointment")

@login_required
def BedCreate(request,username):
    context={}
    patient = Patient.objects.filter(username__iexact=username).first()
    if request.method == 'POST':
        form = BedCreateForm(request.POST,instance=patient)
        if form.is_valid():
            form.save(commit=False)
            bed=authenticate(request)
            bed=Bed.objects.create(patient=patient)
            bed.save()
            form.save()
            messages.success(request,'bed booked')
            return redirect('chms:list_bed',username=username)
    else:
        form = BedCreateForm()
    context['form']=form
    return render(request,'chms/bed_create.html',context)

def BedListView(request,username):
    context={}
    patient = Patient.objects.filter(username__iexact=username)
    bed=Bed.objects.all()
    context['bed']=bed
    return render(request,'chms/bed_list.html',context)

def BedDeleteView(request,pk):
    bed=Bed.objects.get(pk=pk)
    bed.delete()
    return redirect("chms:list_bed",pk)

#@login_required(login_url='login')
#def BedCreate(request):
#    context={}
#    patient=Patient.objects.order_by("fname")
#    if request.method == 'POST':
#        form = BedCreateForm(request.POST)
#        if form.is_valid():
#            form.save(commit=False)
#            bed=Bed.objects.create(patient=patient)
#            message.success(request,'bed created')
#            return redirect('chms:bed_detail')
#    else:
#        form = BedCreateForm()
#    context={'patient':patient,'form':form}
#    return render(request,'chms/bed_create.html',context)

class createInvoice():
    pass
