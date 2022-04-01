from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

from chms.models import Patient,Doctor,Appointment,Bed
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,FormView
from chms.forms import PatientCreateForm,DoctorCreateForm
from django.urls import reverse_lazy

def PatientCreate(request):
    context={}
    if request.method == 'POST':
        form=PatientCreateForm(request.POST)
        if form.is_valid():
            patient=form.save()
            patient.save()
    else:
        form=PatientCreateForm()
        context['form']=form
        return render(request,"chms/register.html", context)
    #def get(self,reqeust,*args,**kwargs):
    #    form=self.form_class()

    #def post(self,request,*args,**kwargs):
    #    form=PatientCreateForm(request.POST)
    #    if form.is_valid():
    #        patient=form.save()
    #        patient.save()
    #    success_url=reverse_lazy('login')
    #    return render(request,'self.template_name',{'form':form})

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
