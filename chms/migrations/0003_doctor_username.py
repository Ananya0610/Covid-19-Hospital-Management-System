# Generated by Django 4.0.3 on 2022-04-28 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chms', '0002_alter_appointment_doctor'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='username',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
