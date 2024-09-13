# Generated by Django 5.1.1 on 2024-09-12 06:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0002_firestation_hospital'),
        ('users', '0012_ticket_firetruck_id_ticket_hospital_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='police_station_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='departments.policestation'),
        ),
    ]