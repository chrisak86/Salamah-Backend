from rest_framework import serializers
from ..models import PoliceStation

class PoliceStationSerializer(serializers.ModelSerializer):
    class Meta:
        model=PoliceStation
        fields=['id', 'status', 'location', 'longitude', 'latitude','police_station_name']