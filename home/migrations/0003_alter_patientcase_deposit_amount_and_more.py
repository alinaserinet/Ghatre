# Generated by Django 4.2.7 on 2023-11-24 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_othersupporters_othersupporter_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientcase',
            name='deposit_amount',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='patientcase',
            name='income_expenses_description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='patientcase',
            name='marital_status_description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='patientcase',
            name='private_insurance_name',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='patientcase',
            name='rent_amount',
            field=models.IntegerField(blank=True),
        ),
    ]
