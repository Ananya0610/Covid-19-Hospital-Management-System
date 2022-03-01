# Generated by Django 4.0.2 on 2022-02-28 16:33

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bed_number', models.CharField(max_length=50)),
                ('room_type', multiselectfield.db.fields.MultiSelectField(choices=[(1, 'PRIVATE ROOM'), (2, 'EMEREGENCY WARD'), (3, 'COVID-19 WARD'), (4, '3-BED SHARED')], max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=20)),
                ('lname', models.CharField(max_length=20)),
                ('gnd', multiselectfield.db.fields.MultiSelectField(choices=[(1, 'FEMALE'), (2, 'MALE'), (3, 'OTHER')], max_length=5)),
                ('ph_no', models.CharField(max_length=15, unique=True)),
                ('email_id', models.EmailField(max_length=254, unique=True)),
                ('specialist', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sdate', models.DateTimeField()),
                ('stime', models.DateTimeField()),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chms.doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=20)),
                ('lname', models.CharField(max_length=20)),
                ('dob', models.DateField(null=True)),
                ('age', models.PositiveIntegerField(blank=True, null=True)),
                ('blood_grp', multiselectfield.db.fields.MultiSelectField(choices=[(1, 'A+'), (2, 'A-'), (3, 'B+'), (4, 'B−'), (5, 'AB+'), (6, 'AB−'), (7, 'O+'), (8, 'O−')], max_length=15, null=True)),
                ('gnd', multiselectfield.db.fields.MultiSelectField(choices=[(1, 'FEMALE'), (2, 'MALE'), (3, 'OTHER')], max_length=5)),
                ('ph_no', models.CharField(max_length=15, unique=True)),
                ('email_id', models.CharField(max_length=50, unique=True)),
                ('vacc_sts', models.CharField(max_length=20)),
                ('doctor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='chms.doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_date', models.DateTimeField()),
                ('app_time', models.DateTimeField()),
                ('desc', models.TextField()),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chms.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chms.patient')),
            ],
        ),
    ]
