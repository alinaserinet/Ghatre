# Generated by Django 5.0.3 on 2024-05-16 19:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_remove_medicalrecord_creator_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicalrecord',
            name='diagnosis_year',
        ),
        migrations.RemoveField(
            model_name='medicalrecord',
            name='disease_name',
        ),
        migrations.RemoveField(
            model_name='medicalrecord',
            name='disease_type',
        ),
        migrations.CreateModel(
            name='DiseaseRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Created At')),
                ('modified_at', models.DateField(auto_now=True, verbose_name='Modified At')),
                ('next_intake', models.CharField(blank=True, max_length=100, verbose_name='Next Intake')),
                ('prescription_cost', models.IntegerField(blank=True, null=True, verbose_name='Prescription Cost')),
                ('patient_claimed_cost', models.IntegerField(blank=True, null=True, verbose_name='Patient Claimed Cost')),
                ('pharmacy', models.CharField(blank=True, max_length=255, verbose_name='Pharmacy')),
                ('recipient', models.CharField(blank=True, max_length=100, verbose_name='Recipient')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('created_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('patient_case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.patientcase', verbose_name='Patient Case')),
            ],
            options={
                'verbose_name': 'Disease Record',
                'verbose_name_plural': 'Disease Records',
            },
        ),
        migrations.CreateModel(
            name='PatientDisease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Created At')),
                ('modified_at', models.DateField(auto_now=True, verbose_name='Modified At')),
                ('disease_type', models.CharField(choices=[('infectious_and_parasitic', 'عفونی و انگلی'), ('cancer_and_blood_diseases', 'سرطان و بیماری های خونی'), ('safety_system', 'سیستم ایمنی'), ('glands', 'غدد'), ('psychiatry', 'اعصاب و روان'), ('neurology', 'مغز و اعصاب'), ('eye_disease', 'بیماری چشمی'), ('ear_nose_throat', 'گوش و حلق و بینی'), ('cardiovascular', 'قلبی-عروقی'), ('respiratory', 'تنفسی'), ('digestive', 'گوارشی'), ('skin', 'پوستی'), ('susculoskeletal', 'عضلانی-اسکلتی'), ('kidney_genitourinary_tract', 'کلیه و مجاری ادراری-تناسلی'), ('gynecology', 'زنان و زایمان\xa0'), ('genetic', 'ژنتیکی و مادرزادی\xa0'), ('accidents', 'سوانح'), ('other', 'سایر')], max_length=30, verbose_name='Disease Type')),
                ('disease_name', models.CharField(max_length=255, verbose_name='Disease Name')),
                ('diagnosis_year', models.IntegerField(verbose_name='Diagnosis Year')),
                ('status', models.CharField(choices=[('in_progress', 'Treatment In Progress'), ('stopped', 'Treatment Stopped'), ('cured', 'Cured')], max_length=20, verbose_name='Status')),
                ('created_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('disease_record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.diseaserecord', verbose_name='Disease Record')),
            ],
            options={
                'verbose_name': 'Patient Disease',
                'verbose_name_plural': 'Patient Diseases',
            },
        ),
        migrations.CreateModel(
            name='PatientDoctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Created At')),
                ('modified_at', models.DateField(auto_now=True, verbose_name='Modified At')),
                ('doctor_name', models.CharField(blank=True, max_length=255, verbose_name='Doctor Name')),
                ('treatment_facilities', models.CharField(blank=True, max_length=255, verbose_name='Treatment Facilities')),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], max_length=20, verbose_name='Status')),
                ('created_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('disease_record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.diseaserecord', verbose_name='Disease Record')),
            ],
            options={
                'verbose_name': 'Patient Doctor',
                'verbose_name_plural': 'Patient Doctors',
            },
        ),
        migrations.CreateModel(
            name='PatientDrugRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Created At')),
                ('modified_at', models.DateField(auto_now=True, verbose_name='Modified At')),
                ('usage_start', models.CharField(max_length=30, verbose_name='Usage Start')),
                ('usage_duration', models.CharField(max_length=30, verbose_name='Usage Duration')),
                ('usage_instruction', models.CharField(max_length=30, verbose_name='Usage Instruction')),
                ('costs', models.IntegerField(blank=True, null=True, verbose_name='Costs')),
                ('costs_without_insurance', models.IntegerField(blank=True, null=True, verbose_name='Costs Without Insurance')),
                ('list_status', models.CharField(choices=[('single_prescription', 'Single Prescription'), ('without_insurance', 'Without Insurance'), ('other', 'Other')], max_length=20, verbose_name='List Status')),
                ('help_needed', models.BooleanField(verbose_name='Help Needed')),
                ('intake_intervals', models.CharField(max_length=100, verbose_name='Intake Intervals')),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], max_length=20, verbose_name='Status')),
                ('disease_record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.diseaserecord', verbose_name='Disease Record')),
                ('drug_brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.drugbrand', verbose_name='Drug Brand')),
                ('generic_drug', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.genericdrug', verbose_name='Generic Drug')),
            ],
            options={
                'verbose_name': 'Patient Drug Record',
                'verbose_name_plural': 'Patient Drug Records',
            },
        ),
        migrations.DeleteModel(
            name='PatientDrug',
        ),
    ]
