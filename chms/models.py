from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField

# Create your models here.
class Patient(models.Model):
    pid=models.AutoField(primary_key=True)
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
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
    email_id=models.CharField(max_length=50, unique=True)
    vacc_sts=models.CharField(max_length=20)

    def __str__(self):
        return self.fname+" "+self.lname

class Doctor(models.Model):
    did=models.AutoField(primary_key=True)
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
    bid=models.AutoField(primary_key=True)
    rtype=(
           (1,'PRIVATE ROOM'),
           (2,'EMEREGENCY WARD'),
           (3,'COVID-19 WARD'),
           (4,'3-BED SHARED'),
    )
    bed_number=models.CharField(max_length=50)
    room_type=MultiSelectField(choices=rtype)


    def __str__(self):
        return bed_number

class Appointment(models.Model):
    pid = models.ForeignKey("Patient", on_delete=models.CASCADE)
    did = models.ForeignKey("Doctor", on_delete=models.CASCADE)
    aid=models.AutoField(primary_key=True)
    app_date=models.DateTimeField(null=False)
    app_time=models.DateTimeField(null=False)
    desc=models.TextField()


class Shift(models.Model):
    sid=models.AutoField(primary_key=True)
    did = models.ForeignKey("Doctor", on_delete=models.CASCADE)
    sdate=models.DateTimeField(null=False)
    stime=models.DateTimeField()
