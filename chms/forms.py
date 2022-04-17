from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from . import models


class PatientCreateForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)
    #assignedDoctor=forms.ModelChoiceField(queryset=models.Doctor.objects.all().filter(),empty_label="Name and Department")
    class Meta:
        model = models.Patient
        fields = ['fname','lname','username','dob','age','blood_grp','gnd','ph_no','email_id','vacc_sts']

        def save(self, commit=True):
            user = super(PatientCreateForm, self).save(commit=False)
            user.username = self.cleaned_data["username"]
            user.password=self.cleaned_data['password']
            if commit:
                user.save()
            return user

class PatientUpdateForm(forms.ModelForm):
    model=models.Patient
    fields= ['fname','lname','dob','age','blood_grp','doctor','gnd','ph_no','email_id','vacc_sts']

class DoctorCreateForm(forms.ModelForm):
    class Meta:
        model = models.Doctor
        fields = ['fname','lname','gnd','ph_no','email_id','specialist']

class AppointmentCreateForm(forms.ModelForm):
    class Meta:
        model = models.Appointment
        fields = ['patient','app_date','app_time','desc']

class BedCreateForm(forms.ModelForm):
    class Meta:
        model = models.Bed
        fields = ['patient','room_type','bed_number']

class ShiftsCreateForm(forms.ModelForm):
    class Meta:
        model = models.Shift
        fields = ['doctor','sdate','stime']
