from django.contrib import admin
from chms.models import Patient,Doctor,Appointment,Bed,Shift
# Register your models here.
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(Bed)
admin.site.register(Shift)
