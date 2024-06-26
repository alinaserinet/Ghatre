# Generated by Django 5.0.3 on 2024-05-16 18:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_remove_patientcase_social_insurance_number_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicalrecord',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='medicalrecord',
            name='second_disease_name',
        ),
        migrations.AddField(
            model_name='medicalrecord',
            name='created_by',
            field=models.ForeignKey(default=1, editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='RelativeDisease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Created At')),
                ('modified_at', models.DateField(auto_now=True, verbose_name='Modified At')),
                ('relation', models.CharField(max_length=255, verbose_name='Relation')),
                ('disease_name', models.CharField(max_length=255, verbose_name='Disease Name')),
                ('infection_age', models.IntegerField(verbose_name='Infection Age')),
                ('current_health_status', models.CharField(max_length=255, verbose_name='Current Health Status')),
                ('medical_record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.medicalrecord', verbose_name='Medical Record')),
            ],
            options={
                'verbose_name': 'Relative Disease',
                'verbose_name_plural': 'Relative Diseases',
            },
        ),
    ]
