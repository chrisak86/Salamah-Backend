from rest_framework import serializers
from ..models import FireStation

class FireStationSerializer(serializers.ModelSerializer):
    class Meta:
        model=FireStation
        fields=['id', 'status', 'location', 'longitude', 'latitude','fire_station_name']