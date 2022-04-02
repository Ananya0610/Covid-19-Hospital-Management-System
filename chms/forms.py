from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from chms.models import Patient,Doctor,Appointment,Bed,Shift
class PatientCreateForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['fname','lname','dob','age','blood_grp','doctor','gnd','ph_no','email_id','vacc_sts']

class PatientUpdateForm(forms.ModelForm):
    model=Patient
    fields= ['fname','lname','dob','age','blood_grp','doctor','gnd','ph_no','email_id','vacc_sts']

class DoctorCreateForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['fname','lname','gnd','ph_no','email_id','specialist']

class AppointmentCreateForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['patient','doctor','app_date','app_time','desc']

class BedCreateForm(forms.ModelForm):
    class Meta:
        model = Bed
        fields = ['patient','room_type','bed_number']

class ShiftsCreateForm(forms.ModelForm):
    class Meta:
        model = Shift
        fields = ['doctor','sdate','stime']
