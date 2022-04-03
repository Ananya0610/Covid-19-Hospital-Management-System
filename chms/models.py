from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User=get_user_model()
from multiselectfield import MultiSelectField
from django.contrib import auth
# Create your models here.

class User(auth.models.User,auth.models.PermissionsMixin):
    def __str__(self):
        return "@{}".format(self.username)

class Patient(models.Model):
    #user = models.OneToOneField(User,primary_key=True,related_name='patient',on_delete=models.CASCADE)
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    #username=models.CharField(max_length=50,null=True)
    username = models.CharField(max_length=100)
    dob = models.DateField(null=True)
    age=models.PositiveIntegerField(null=True, blank=True)
    bld_grp=(
            (1, 'A+'),
            (2, 'A-'),
            (3, 'B+'),
            (4, 'B−'),
            (5, 'AB+'),
            (6,'AB−'),
            (7,'O+'),
            (8,'O−'))
    blood_grp=MultiSelectField(choices=bld_grp, null=True)
    doctor = models.ForeignKey("Doctor", on_delete=models.CASCADE, null=True)
    gender=(
        (1,'FEMALE'),
        (2,'MALE'),
        (3,'OTHER'),
        )
    gnd=MultiSelectField(choices=gender)
    ph_no=models.CharField(max_length=15,null=False, blank=False, unique=True)
    email_id=models.EmailField(max_length=50, unique=True)
    vacc_sts=models.CharField(max_length=20)

    def __str__(self):
        return self.fname+" "+self.lname

class Doctor(models.Model):
    #user = models.OneToOneField(User,null=True,primary_key=True,related_name='doctor',on_delete=models.CASCADE)
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    gender=(
        (1,'FEMALE'),
        (2,'MALE'),
        (3,'OTHER'),
        )
    gnd=MultiSelectField(choices=gender)
    ph_no=models.CharField(max_length=15,null=False, blank=False, unique=True)
    email_id=models.EmailField(max_length=254, unique=True)
    specialist=models.CharField(max_length=20)

    def __str__(self):
        return self.fname+" "+self.lname

class Bed(models.Model):
    bed_number=models.CharField(max_length=50)
    patient= models.ForeignKey("Patient", on_delete=models.CASCADE,null=True)
    rtype=(
           (1,'PRIVATE ROOM'),
           (2,'EMEREGENCY WARD'),
           (3,'COVID-19 WARD'),
           (4,'3-BED SHARED'),
    )
    room_type=MultiSelectField(choices=rtype)
    def __str__(self):
        return bed_number

class Appointment(models.Model):
    patient = models.ForeignKey("Patient", on_delete=models.CASCADE,null=True)
    doctor= models.ForeignKey("Doctor", on_delete=models.CASCADE,null=True)
    app_date=models.DateTimeField(null=False)
    app_time=models.DateTimeField(null=False)
    desc=models.TextField()


class Shift(models.Model):
    doctor = models.ForeignKey("Doctor",null=True, on_delete=models.CASCADE)
    sdate=models.DateTimeField(null=False)
    stime=models.DateTimeField()
