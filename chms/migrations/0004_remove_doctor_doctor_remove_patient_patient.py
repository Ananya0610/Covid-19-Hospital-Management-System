# Generated by Django 4.0.1 on 2022-04-02 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chms', '0003_alter_appointment_doctor_alter_appointment_patient_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='doctor',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='patient',
        ),
    ]
