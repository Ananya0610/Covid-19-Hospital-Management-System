from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from . import models
from chms.models import Patient
class PatientCreateForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)
    class Meta:
        model = models.Patient
        fields = ['fname','lname','username','dob','age','blood_grp','gnd','ph_no','email_id','vacc_sts']

        def save(self, commit=True):
            user = super(PatientCreateForm,self).save(commit=False)
            user.username = self.cleaned_data["username"]
            user.password=self.cleaned_data['password']
            if commit:
                user.save()
            return user

class DoctorCreateForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)
    class Meta:
        model = models.Doctor
        fields = ['fname','lname','username','gnd','ph_no','email_id','specialist']

        def save(self, commit=True):
            user = super(DoctorCreateForm, self).save(commit=False)
            user.username = self.cleaned_data["username"]
            user.password=self.cleaned_data['password']
            if commit:
                user.save()
            return user

class AppointmentCreateForm(forms.ModelForm):
    #patient= forms.ModelMultipleChoiceField(queryset=Patient.objects.all())
    class Meta:
        model = models.Appointment
        fields = ['patient','app_date','app_time','desc']

        def save(self, commit=True):
            appointment = super(AppointmentCreateForm,self).save(commit=False)
            if commit:
                appointment.save()
            return appointment


class BedCreateForm(forms.ModelForm):
    class Meta:
        model = models.Bed
        fields = ['bed_number','patient','room_type']

        def save(self, commit=True):
            bed = super(BedCreateForm, self).save(commit=False)
            #user.username = self.cleaned_data["username"]
            #user.password=self.cleaned_data['password']
            if commit:
                bed.save()
            return bed

class ShiftsCreateForm(forms.ModelForm):
    class Meta:
        model = models.Shift
        fields = ['doctor','sdate','stime']
