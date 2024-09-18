from django.db import models
from django.contrib.auth.models import AbstractUser
from .custom_managers.custom_user_manager import CustomUserManager
from ..departments.models import PoliceStation,Hospital,FireStation
from django.utils import timezone
import pytz

class CustomUser(AbstractUser):
    GENDER_CHOICES = (
        ('MALE', 'MALE'),
        ('FEMALE', 'FEMALE'),
    )

    TYPE_CHOICES = (
        ('USER','USER'),
        ('POLICE', 'POLICE'),
    )
    

    username=None
    email=models.EmailField(unique=True)
    civil_id=models.CharField(max_length=100, default=None)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='male')
    user_type = models.CharField(max_length=10, choices=TYPE_CHOICES, default="user")
    is_approved=models.BooleanField(default=False) 
    is_online=models.BooleanField(default=False)  
    


    USERNAME_FIELD="email"
    REQUIRED_FIELDS=[]

    objects=CustomUserManager()

    def __str__(self):
        return self.email
    
class PoliceOfficerPoliceStaion(models.Model):
    user=models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    police_station=models.ForeignKey(PoliceStation, on_delete=models.CASCADE, null=True)

    def __str__(self):
        strg=str(self.id)
        return strg
    

class Ticket(models.Model): 
    TYPE_CHOICES = (
        ('AMBULANCE','AMBULANCE'),
        ('FIRETRUCK', 'FIRETRUCK'),
        ('ACCIDENT', 'ACCIDENT'),

    )
    
    user_id=models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='USER')
    user_name=models.CharField(max_length=50, default='user')
    eta=models.CharField(max_length=50)
    hospital_id=models.ForeignKey(Hospital, on_delete=models.CASCADE,blank=True, null=True)
    firetruck_id=models.ForeignKey(FireStation, on_delete=models.CASCADE,blank=True, null=True)
    distance=models.CharField(max_length=50)
    police_station_name=models.CharField(max_length=50, blank=True, null=True)
    fire_station_name=models.CharField(max_length=50, blank=True, null=True)
    hospital_name=models.CharField(max_length=50, blank=True, null=True)
    police_station_id=models.ForeignKey(PoliceStation, on_delete=models.CASCADE,blank=True, null=True)
    attend_id=models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='POLICE', blank=True, null=True)
    user_lat=models.FloatField()
    user_long=models.FloatField()
    dest_lat=models.FloatField()
    dest_long=models.FloatField()
    completed=models.BooleanField(default=False)
    type_choice=models.CharField(max_length=50, choices=TYPE_CHOICES)
    cancel = models.BooleanField(null=True, blank=True)
    reason = models.CharField(max_length=2000, null=True, blank=True)
    


class ModelLogs(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    lat = models.FloatField()
    lng = models.FloatField()
    response = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        gmt_plus_3 = pytz.timezone('Europe/Istanbul')
        now = timezone.now()
        if not self.pk:  # Only set created_at on creation
            self.created_at = now.astimezone(gmt_plus_3)
        self.updated_at = now.astimezone(gmt_plus_3)
        super().save(*args, **kwargs)
    
