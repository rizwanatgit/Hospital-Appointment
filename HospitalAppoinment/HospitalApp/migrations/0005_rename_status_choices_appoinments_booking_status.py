# Generated by Django 3.2.25 on 2024-10-28 06:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HospitalApp', '0004_appoinments_status_choices'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appoinments',
            old_name='status_choices',
            new_name='booking_status',
        ),
    ]