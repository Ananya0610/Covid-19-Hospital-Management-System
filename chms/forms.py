from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from chms.models import Patient,Doctor,Appointment,Bed
class PatientCreateForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'


class DoctorCreate(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'

class AppointmentCreate(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'

class BedCreate(forms.ModelForm):
    class Meta:
        model = Bed
        fields = '__all__'
