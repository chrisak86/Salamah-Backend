from django.db import models

class PoliceStation(models.Model):
    status=models.BooleanField(default=True)
    location=models.CharField(max_length=50)
    longitude=models.FloatField()
    latitude=models.FloatField()
    police_station_name=models.CharField(max_length=500)


class Hospital(models.Model):
    status=models.BooleanField(default=True)
    location=models.CharField(max_length=50)
    longitude=models.FloatField()
    latitude=models.FloatField()
    hospital_name=models.CharField(max_length=500)

class FireStation(models.Model):
    status=models.BooleanField(default=True)
    location=models.CharField(max_length=50)
    longitude=models.FloatField()
    latitude=models.FloatField()
    fire_station_name=models.CharField(max_length=500)