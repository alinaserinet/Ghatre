# Generated by Django 5.0.3 on 2024-05-17 18:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_remove_patientdisease_created_by_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicalrecord',
            name='doctors_names',
        ),
        migrations.RemoveField(
            model_name='medicalrecord',
            name='treatment_facilities',
        ),
    ]
